n = int(input())
a = []
b = []

for i in range(n):
    x, y = map(int,input().split())
    a.append(x)
    b.append(y)

ans = 0

for i in range(n):
    if (ans+a[-1-i])%b[-1-i] == 0:
        continue
    ans += b[-1-i]-(ans+a[-1-i])%b[-1-i]

print(ans)
