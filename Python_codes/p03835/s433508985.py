k , s = map(int , input().split())
ans=0
for i in range(0 , k+1):
	for j in range(0 , k+1):
		if i+j<=s and (s-(i+j))<=k:
			ans =ans+1
print(ans)