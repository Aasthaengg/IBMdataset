#48 ABC128E
#イベントソート   
import sys
input = sys.stdin.readline

n,q=map(int,input().split())
stx=[list(map(int,input().split())) for _ in range(n)]
d=[int(input()) for _ in range(q)]

stx=sorted(stx,key=lambda x:x[2])

ans=[-1 for _ in range(q)]
skip=[-1 for _ in range(q)]

from bisect import bisect_left

for s,t,x in stx:
	left=bisect_left(d,s-x)
	right=bisect_left(d,t-x)
	while left<right:
		if skip[left]==-1:
			ans[left]=x
			skip[left]=right
			left+=1
		else:
			left=skip[left]
print('\n'.join(map(str,ans)))