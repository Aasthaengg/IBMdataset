n=int(input())
A=list(map(int,input().split()))
#全パターンは3**n
x=1
for i in range(n):
    if A[i]%2==0:
        x*=2
    else:
        x*=1
print(3**n-x)