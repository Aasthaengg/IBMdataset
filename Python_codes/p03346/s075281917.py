import sys
input=sys.stdin.readline
n=int(input())
p=[int(input())for _ in range(n)]
num=[-1]*n
for i in range(n):
	num[p[i]-1]=i
ans=0
kari=1
for i in range(n-1):
	if num[i+1]>num[i]:
		kari+=1
	else:
		ans=max(ans,kari)
		kari=1
ans=max(ans,kari)
print(n-ans)