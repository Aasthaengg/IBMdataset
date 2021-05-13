n,k=map(int,input().split())
# 累積和！max-min+1
csl=[]
sum=0
for i in range(n+1):
	sum+=i
	csl.append(sum)
#3 2
#[0, 1, 3, 6]
# 0 1 2 3
cnt=0
for i in range(k,n+1):
	max=csl[n]-csl[n-i]
	min=csl[i-1]
	#初めの数も含むの+1
	cnt+=(max-min+1)
	cnt%=(10**9+7)
#0~nまで全選択の+1
print(cnt+1)