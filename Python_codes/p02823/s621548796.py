n,a,b=map(int,input().split())
ans=0
if (b-a)%2 == 0:
	ans = (b-a)//2
else:
	if (b-1) < (n-a):
		ans = min(n-a, b-1, a+(b-a-1)//2)
	else:
		ans = min(n-a, b-1, n-b+1+(b-a-1)//2)
print(ans)