import sys
sys.setrecursionlimit(10**5 + 9)
from collections import defaultdict
dp=defaultdict(lambda:0)
n=int(input())
ar,br,cr=[0]*n,[0]*n,[0]*n

for i in range(n):
	ar[i],br[i],cr[i]=map(int,input().split())
if n==1:
	print(max(ar[0],br[0],cr[0]))
	exit()
def points(i,pv):
	if dp[(i,pv)] != 0:
		return dp[(i,pv)]
	if pv==1:
		x,y=br[i],cr[i]
		a,b=2,3
	elif pv==2:
		x,y=ar[i],cr[i]
		a,b=1,3
	else:
		x,y=ar[i],br[i]
		a,b=1,2
	if i==n-1:
		return max(x,y)
	ax=points(i+1,a)+x
	by=points(i+1,b)+y
	ans=max(by,ax)
	dp[(i,pv)]=ans
	return ans
p=points(1,1)+ar[0]
q=points(1,2)+br[0]
r=points(1,3)+cr[0]
print(max(p,q,r))

	
		

