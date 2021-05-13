a=int(input())
b=input()
b=list(b)
c=[0]*26
ans=0
t=0
for i in range(a):
	c[ord(b[i])-97]=c[ord(b[i])-97]+1

for j in range(26):
	t=c[j]
	for k in range(j+1,26):
		t=t*(c[k]+1)
	ans=ans+t
print(ans%(10**9+7))