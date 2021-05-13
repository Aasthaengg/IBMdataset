N=int(input())
A=list(map(int,input().split()))
for i in range(N):
    x=A[i]
    y=0
    while x%2==0:
        x//=2
        y+=1
    A[i]=y
print(min(A))
