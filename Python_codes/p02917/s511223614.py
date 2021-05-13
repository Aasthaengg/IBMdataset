n=int(input())
b=list(map(int,input().split()))
a=[float('Inf')]*n
for i,num in enumerate(b):
	if n>i:
		a[i]=min(a[i],num)
		a[i+1]=num
print(sum(a))