n,m = map(int,input().split())
drink = []
for _ in range(n):
    a,b = map(int,input().split())
    drink.append((a,b))
d = sorted(drink)

ans = 0
x = 0

for t in d:
    if x+t[1] < m:
        ans += t[0]*t[1]
        x += t[1]
    else:
        ans += t[0]*(m-x)
        break

print (ans)
