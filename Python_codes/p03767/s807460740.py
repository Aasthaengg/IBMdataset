N = int(input())
a = list(map(int,input().split()))
a.sort(reverse= True)
ans =0
for n in range(1,N+1):
	ans = ans+a[2*n-1]
print(ans)