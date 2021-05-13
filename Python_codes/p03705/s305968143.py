N,A,B=map(int,input().split())

m=A*(N-1)+B
M=A+B*(N-1)
ans=M-m+1
ans=max(ans,0)
print(ans)