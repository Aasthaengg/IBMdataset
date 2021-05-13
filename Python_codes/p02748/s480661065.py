A, B, M = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
XYC = [[int(x) for x in input().split()] for _ in range(M)]

ans = min(a) + min(b)

for x, y, c in XYC:
    ans = min(ans, a[x - 1] + b[y - 1] - c)

print(ans)

