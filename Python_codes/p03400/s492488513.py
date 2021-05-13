N=int(input())
D,X=map(int,input().split())
A=[int(input()) for _ in range(N)]
 
ans=0
 
for i in range(len(A)):
    ans += (D-1)//A[i]+1
print(ans+X)