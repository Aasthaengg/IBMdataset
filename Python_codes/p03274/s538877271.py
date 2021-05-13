import bisect

N, K = map(int,input().split())
X = list(map(int,input().split()))

s = bisect.bisect_left(X,0)
if 0 in X:
    K -= 1
else:
    bisect.insort_left(X,0)
    N += 1

MIN = 2 * 10**9
for i in range(K+1):
    if s - K + i >= 0 and s + i <N:
        f = X[s -K+i]
        l = X[s+i]
        if abs(f) < abs(l):
            ans = abs(f) * 2 + abs(l)
        else:
            ans = abs(l) * 2 + abs(f)
        MIN =min(MIN,ans)

print(MIN)