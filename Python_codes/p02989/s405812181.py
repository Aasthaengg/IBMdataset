n = int(input())
D = list(map(int, input().split()))
D.sort()

d1, d2 = D[n // 2 - 1], D[n // 2]
ans = 0
if d1 != d2:
    ans = len(range(d1 + 1, d2 + 1))

print(ans)