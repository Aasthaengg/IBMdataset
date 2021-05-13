n=int(input())
a=list(map(int,input().split()))
ans=3**n
cnt=0
for i in range(n):
  if a[i]%2==0:
    cnt=cnt+1
print(ans-2**cnt)