n = int(input())

D = []

for i in range(n):
    a, b = map(int, input().split())
    D.append([a+b, a, b])

D.sort(reverse=True)

ans = 0
for i in range(n):
    if i % 2 == 0:
        ans += D[i][1]
    else:
        ans -= D[i][2]

print(ans)
