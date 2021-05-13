N=int(input())
C=[list(map(int,input().split()))for i in range(2)]
ans=0
for i in range(N):
	tmp=sum(C[0][:i+1])+sum(C[1][i:])
	if ans<tmp:
		ans=tmp
print(ans)