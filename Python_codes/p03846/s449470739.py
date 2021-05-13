n = int(input())
arr = list(map(int , input().split()))
mod = 10**9+7
h = [0 for i in range(0,n)]
for i in range(0,n):
	h[arr[i]]=h[arr[i]]+1
	if n%2==0 and arr[i]==0:
		print(0)
		exit()
ans=1
if n%2:
	for i in range(2 ,n, 2):
		if h[i]!=2:
			print(0)
			exit()
		ans = (ans*2)%mod
else:
	for i in range(1, n , 2):
		if h[i]!=2:
			print(0)
			exit()
		ans = (ans*2)%mod
print(ans)