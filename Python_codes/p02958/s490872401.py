from sys import exit
n=int(input())
p=list(map(int,input().split()))
s=sorted(p)
if p==s:
	print("YES")
	exit(0)
for i in range(n-1):
	for j in range(i+1,n):
		p[i],p[j] = p[j],p[i]
		if p == s:
			print("YES")
			exit(0)
		p[i],p[j] = p[j],p[i]
print("NO")