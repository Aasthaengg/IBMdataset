n, h =map(int, input().split())
A=[]
B=[]
w=0
sub=0
for i in range(n):
	a,b=map(int, input().split())
	A.append(a)
	B.append(b)
	w=max(a,w)

ans=0
B.sort(reverse=True)
for i in range(n):
	if B[i]>w:
		h-=B[i]
		ans+=1
		if 1>h:
			print(ans)
			exit()
ans+=h//w
if h%w==0:
	print(ans)
else:
	print(ans+1)
