N, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
res = 0
for i, a in enumerate(A):
    x -= a
    if x >= 0:
        res += 1
    else:
        break
else:
    if x > 0:
        res -= 1
print(res)

