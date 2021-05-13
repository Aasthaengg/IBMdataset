N = int(input())
C = dict()
i, cp, hist, ans = 0, 0, [0]*N, 0
for _ in range(N):
    c = int(input())
    if c != cp:
        if c in C.keys():
            temp = hist[C[c]] + 1
            hist[i] = hist[i-1] + temp
            ans += temp
        else:
            hist[i] += hist[i-1]
        C[c], cp = i, c
        i += 1
print((ans+1) % (10**9+7))