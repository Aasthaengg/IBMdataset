s = input()
ans =0
n = len(s)
for i in range(1 , n):
	f=0
	for j in range(0 , i-1):
		if j+i>=n or s[j]!=s[i+j]:
			f=1
	if f==0:
		if n-2*i!=0:
			ans = max(ans, 2*i)
print(ans)