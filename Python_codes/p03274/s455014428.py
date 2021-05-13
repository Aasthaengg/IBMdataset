n, k = map(int, input().split())
L, R = [], []
for x in map(int, input().split()):
    if x < 0:
        L.append(-x)
    else:
        R.append(x)
L.reverse()
INF = 10**18
ans = INF
if len(L) == 0:
    ans = R[k-1]
elif len(R) == 0:
    ans = L[k-1]
else:
    for i in range(1, k):
        l, r = k-i-1, i-1
        if not(l < len(L)) or not(r < len(R)):
            continue
        a, b = L[l], R[r]
        ans = min(ans, min(a, b)+a+b)
print(ans)
