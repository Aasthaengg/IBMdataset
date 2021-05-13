n,a,b = map(int,input().split())
ans = 0
q = n // (a+b)

ans += q*a
q = n - (a+b)*q

if q - a >= 0:
    ans += a
if q - a < 0:
    ans = ans + a +(q-a)
print(ans)
