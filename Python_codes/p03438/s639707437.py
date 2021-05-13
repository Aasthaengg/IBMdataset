n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sousa=sum(b)-sum(a)
cnt=0
for i in range(n):
	if b[i]>a[i]:
		cnt+=(b[i]-a[i]+1)//2
if sousa>=cnt:
	print("Yes")
else:
	print("No")