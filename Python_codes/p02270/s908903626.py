N, K = map(int, input().split())
lst = [int(input()) for i in range(N)]

def num_luggage(P, K, lst):
    weight = 0
    n_track = 1
    for i, e in enumerate(lst):
        if (e > P):
            return i
        if (weight + e <= P):
            weight += e
        else:
            n_track += 1
            weight = e
        if (n_track == K+1):
            return i
    return len(lst)

left, right = 0, 10000 * N
i_break = 0
while right - left > 1:
    mid = (left+right)//2
    if N <= num_luggage(mid, K, lst):
        right = mid  # ギリギリOKなのはrightに最終的に格納されているはず
    else:  # 余裕がなければ(n>n_nimotu_if_P())、Pを増やす
        left = mid

print(right)
