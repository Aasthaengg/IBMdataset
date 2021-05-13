N,M = map(int,input().split())
ans=0
ans+=N
M=M-N*2
if(M<0):
	ans = ans - abs(M//2)
if(M>0):
	ans = ans + M//4
print(ans)