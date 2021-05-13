def gcd(x,y):
    while y>0:
        x,y = y,x%y
    return x
N=int(input())
T = [int(input()) for _ in range(N)]
a = T[0]
for i in range(1,N):
    b = T[i]
    c = gcd(a,b)
    a = (a//c)*b
print(a)