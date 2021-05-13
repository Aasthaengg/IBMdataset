import fractions
x, y = map(int, input().split())

ans = -1
for i in range((x*y)//fractions.gcd(x, y), 0, -x):
    if i%y != 0:
        ans = i
        break
print(ans)
