from collections import Counter
n=int(input())
s=input()
c=Counter(s)
ans = c['R'] * c['G'] * c['B']
for i in range(n-2):
	for j in range(i+1,n-1):
		k=j+(j-i)
		if k>=n:
			break
		if s[i]!=s[j]!=s[k]!=s[i]:
			ans -=1
print(ans)
