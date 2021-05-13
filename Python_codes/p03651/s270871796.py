def gcd(x,y):
    while y>0:
        x,y = y,x%y
    return x
N,K = map(int,input().split())
A = sorted(list(map(int,input().split())))
a = A[0]
for i in range(1,N):
    a = gcd(a,A[i])
if K<=A[-1] and K%a==0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")