n = int(input())
R = [int(input()) for _ in range(n)]
ret = -(10 ** 9)
mn = R[0]
for r in R[1:]:
    ret = max(ret, r - mn)
    mn = min(mn, r)
print(ret)