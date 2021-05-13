n=int(input())
t=list(map(int,input().split()))
a=list(map(int,input().split()))
mod=10**9+7
h1=[[-1,-1]for _ in range(n)]
h1[0]=[t[0],t[0]]
for i in range(n-1):
	if t[i+1]>t[i]:
		h1[i+1]=[t[i+1],t[i+1]]
	else:
		h1[i+1]=[1,t[i+1]]
h2=[[-1,-1]for _ in range(n)]
a.reverse()
h2[-1]=[a[0],a[0]]
for i in range(n-1):
	if a[i+1]>a[i]:
		h2[-i-2]=[a[i+1],a[i+1]]
	else:
		h2[-i-2]=[1,a[i+1]]
ans=1
for i in range(n):
	ran=min(h1[i][1],h2[i][1])-max(h1[i][0],h2[i][0])+1
	if ran<=0:
		ans=0
		break
	ans*=ran
	ans%=mod
print(ans if ans>=0 else 0)
