n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(n):
  sum=sum+1/a[i]
print(1/sum)
