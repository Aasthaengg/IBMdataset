n=int(input())
s=n
for i in range(1,n):
	s*=i
	s=s%(10**9+7)
print(s)