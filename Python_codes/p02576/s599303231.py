n,x,t = map(int,input().split(' '))
if n % x == 0:
    k = int(n / x)
else:
    k = n // x +1
print(k*t)