n,a,b = map(int,input().split())
s = a+b
num = n // s
if 0 <= n % s <= a:
    ans = num*a + n % s
else:
    ans = num*a + a
print(ans)