n,m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()
money = 0
drink = 0
for a,b in ab:
    if drink+b <= m:
        drink += b
        money += a*b
    else:
        money += (m-drink) * a
        drink = m
    if drink == m: break
print(money)