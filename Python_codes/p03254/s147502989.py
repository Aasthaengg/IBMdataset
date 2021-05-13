N, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
res = 0
for a in A:
    if a > X:
        break
    res += 1
    X -= a
else:
    if X > 0:
        res -= 1
print(max(res, 0))