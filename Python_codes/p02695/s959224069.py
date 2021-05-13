from itertools import combinations_with_replacement as comb_rplc
n,m,q=map(int,input().split())
a=[0]*q
b=[0]*q
c=[0]*q
d=[0]*q
for i in range(q):
	a[i],b[i],c[i],d[i]=map(int,input().split())
ans=0

def dfs(A):
	ans=0
	if len(A)==n:#数列が完成
		score1=0
		for i in range(q):
			if A[b[i]-1]-A[a[i]-1]==c[i]:
				score1+=d[i]
		return score1
	else:
		for i in range(A[-1],m+1):
			A_next=A+(i,)
			score=dfs(A_next)
			ans=max(ans,score)
	return ans
	
score=dfs((1,))
ans=max(ans,score)
print(ans)