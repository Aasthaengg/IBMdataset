def binary_search(n, arr, target, lower=True):
    flg = True
    cnt = 0
    while flg:
        if n >> cnt:
            cnt += 1
        else:
            flg = False
    if lower:
        if target < arr[0]:
            return -1
        if target >= arr[n-1]:
            return n
        l, r = 0, n
        d = (l + r) // 2
        for i in range(cnt+1):
            if arr[d] <= target:
                l = d
                d = (l + r) // 2
            else:
                r = d
                d = (l + r) // 2
        return d

A, B, Q = map(int, input().split())
S = [-int(1e13)] + [int(input()) for _ in range(A)] + [int(1e13)]
T = [-int(1e13)] + [int(input()) for _ in range(B)] + [int(1e13)]
for i in range(Q):
    x = int(input())
    sl = binary_search(A+2, S, x)
    tl = binary_search(B+2, T, x)
    ll = max(x - S[sl], x - T[tl])
    lr = min(T[tl+1] - x + 2 * (x - S[sl]), 2 * (T[tl+1] - x) + x - S[sl])
    rl = min(S[sl+1] - x + 2 * (x - T[tl]), 2 * (S[sl+1] - x) + x - T[tl])
    rr = max(S[sl+1] - x, T[tl+1] - x)
    print(min(ll, lr, rl, rr))