n=int(input())
f=0
for i in range(1,n+2):
	if i*(i-1)//2==n:
		f=1
		break
if f==0:
	print("No")
	exit()
print("Yes")
print(i)
k=i
cnt=0
s=[[-1]*k for _ in range(k)]
for i in range(k):
	for j in range(k):
		if i<j:
			s[i][j]=cnt
			cnt+=1
ans=[[]for _ in range(k)]
for i in range(k):
	for j in range(k):
		if s[i][j]!=-1:
			ans[i].append(s[i][j]+1)
			ans[j].append(s[i][j]+1)
for x in ans:
	print(k-1,*x)
