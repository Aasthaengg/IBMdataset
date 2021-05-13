import sys
input=sys.stdin.readline
n,m=map(int,input().split())
cnt=[0]*n
for _ in range(m):
	a,b=map(int,input().split())
	cnt[a-1]+=1
	cnt[b-1]+=1
f=1
for i in range(n):
	if cnt[i]%2!=0:
		f=0
		break
print("YES" if f else "NO")