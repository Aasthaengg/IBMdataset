n=int(input())
h=list(map(int,input().split()))
ans=0
hi=0
count=0
for i,num in enumerate(h):
	if i>0:
		if hi>=num:
			count+=1
		else:
			ans=max(ans,count)
			count=0
	hi=num
ans=max(ans,count)
print(ans)