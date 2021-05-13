import collections

n=int(input())
arr=list(map(int,input().split()))
ans=0
cnt=collections.defaultdict(int)
for i in range(1,n+1):
	ans+=cnt[i-arr[i-1]] #すでに見た要素について、i-Aiと等しいものの個数を数える
	cnt[i+arr[i-1]]+=1 #i+Aiを付け加える
print(ans)