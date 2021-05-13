def gcd(x,y):
    while y>0:
        x,y = y,x%y
    return x
N = int(input())
A = list(map(int,input().split()))
cmin = A[0]
for i in range(1,N):
    cmin = gcd(cmin,A[i])
print(cmin)