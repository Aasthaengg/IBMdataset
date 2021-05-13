n = int(input())

abl = []

for _ in range(n):
    a,b = map(int,input().split())
    abl.append((a+b, a, b))

abl = sorted(abl, reverse=True)

ans = 0
for i in range(n):
    if i % 2 == 0:
        ans += abl[i][1]
    else:
        ans -= abl[i][2]

print(ans)


