# coding: utf-8

# https://atcoder.jp/contests/abc107
# 14:34 chudan
# 2020/07/10 retry 12:54-


def main():
    N, K = map(int, input().split())
    xs = list(map(int, input().split()))

    if xs == [0]:
        return 0

    for i in range(N):
        if xs[i] == 0:
            del xs[i]
            N -= 1
            K -= 1
            break

    if xs[0] > 0:
        xs.insert(0, 0)
        s = 0
    elif xs[N-1] < 0:
        xs.append(0)
        s = N
    else:
        for i in range(N-1):
            if xs[i] < 0 and xs[i+1] > 0:
                xs.insert(i+1, 0)
                s = i+1
                break
    N += 1

    candidates = []
    # from left to right
    if s > K-1:
        l = s-K
        r = s
        d = xs[r] - xs[l]
    else:
        l = 0
        r = K
        d = (xs[s] - xs[l]) + (xs[r] - xs[l])
    candidates.append(d)

    # print(candidates)
    while l < s and r < N-1:
        if r == s:
            d = d - (xs[l+1]-xs[l]) + (xs[r+1]-xs[l+1])
        else:
            d = d - 2*(xs[l+1]-xs[l]) + (xs[r+1]-xs[r])
        candidates.append(d)
        # print(l, r, d)
        l += 1
        r += 1

    # print("="*10)
    # from right to left
    if s+K < N:
        l = s
        r = s+K
        d = xs[r] - xs[l]
    else:
        l = N-(K+1)
        r = N-1
        d = (xs[r]-xs[s]) + (xs[r]-xs[l])
    candidates.append(d)

    # print(candidates)
    while l > 0 and r > s:
        if l == s:
            d = d - (xs[r]-xs[r-1]) + (xs[r-1]-xs[l-1])
        else:
            d = d - 2*(xs[r]-xs[r-1]) + (xs[l]-xs[l-1])
        candidates.append(d)
        # print(l, r, d)
        l -= 1
        r -= 1

    # print(candidates)
    return min(candidates)

    # ds = [None] * N
    # for i in range(N):
    #     ds[i] = xs[i+1]-xs[i]


# def main():
#     N, K = map(int, input().split())
#     x = list(map(int, input().split()))

#     if x[-1] <= 0:
#         n_l = N
#         n_r = 0
#         l_start = N-1
#         r_start = None  # all <= 0
#     else:
#         for i in range(N):
#             if x[i] > 0:
#                 n_l = i
#                 n_r = N-i
#                 l_start = i-1 if i > 0 else None  # all > 0
#                 r_start = i
#                 break

#     # left -> right
#     t = []
#     if r_start is None:  # 左に直進するのみ
#         t.append(-x[l_start-K+1])
#     else:
#         n = max(K-n_r, 0)
#         tim = -x[l_start-n+1]*2 + x[K-n]
#         t.append(tim)
#         for n in range(max(K-n_r, 0)+1, n_l+1):
#             tim += 2*(x[l_start-n+1]-x[l_start-n])
#             tim -= x[l_start+K-n]-x[l_start+K-n-1]
#             t.append(tim)

#     # right -> left
#     s = []
#     if l_start is None:  # 右に直進するのみ
#         s.append(x[r_start+K-1])
#     else:
#         m = max(K_n_l, 0)
#         tim = x[r_start+n-1]*2 + 


print(main())
