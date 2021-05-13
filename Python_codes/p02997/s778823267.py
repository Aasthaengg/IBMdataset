n,k=map(int,input().split())
if k>(n-2)*(n-1)//2:
	print(-1)
	exit()
elif k==(n-2)*(n-1)//2:
	print(n-1)
	for i in range(n-1):
		print(1,i+2)
	exit()
ans=[]
for i in range(n-1):
	ans.append((1,i+2))
cnt=(n-2)*(n-1)//2
a=2
b=3
while cnt>k:
	cnt-=1
	ans.append((a,b))
	b+=1
	if b==n+1:
		b=a+2
		a+=1
print(len(ans))
for x in ans:
	print(*x)