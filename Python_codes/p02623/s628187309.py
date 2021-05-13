n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=0
asum=0
bsum=0
pointer=0
while pointer<m and bsum+b[pointer]<=k:
	bsum+=b[pointer]
	pointer+=1
ans=pointer
for i in range(n):
	asum+=a[i]
	while asum+bsum>k and pointer>=0:
		pointer-=1
		bsum-=b[pointer]
	if asum+bsum>k:
		break
	ans=max(ans,(i+1)+pointer)
print(ans)