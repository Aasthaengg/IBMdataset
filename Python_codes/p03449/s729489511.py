n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
ans=sum(a1)+a2[n-1]
sum_a=ans

for i in range(n-1):
  sum_a=sum_a-a1[n-1-i]+a2[n-2-i]
  ans=max(ans,sum_a)
print(ans)


