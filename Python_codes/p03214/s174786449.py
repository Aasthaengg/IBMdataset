N=int(input())
A=[int(i) for i in input().split()]
AVE=sum(A)/N
D=abs(A[-1]-AVE)
ans=N-1
for i in reversed(range(N)):
    d=abs(A[i]-AVE)
    if d<=D:
        ans=i
        D=d
print(ans)