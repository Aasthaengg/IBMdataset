def gcd(x,y):
    while y>0:
        x,y = y,x%y
    return x
N,K = map(int,input().split())
A = list(map(int,input().split()))
a = A[0]
for i in range(1,N):
    a = gcd(a,A[i])
flag = 0
for i in range(N):
    if A[i]>=K:
        b = A[i]-K
        if b%a==0:
            flag = 1
            break
if flag==1:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")