n,k=map(int,input().split())
a=list(map(int,input().split()))
after=0
before=0
for i in range(n):
  for j in range(i+1,n):
    if a[i] > a[j]:
      after += 1
    elif a[i] < a[j]:
      before += 1
print((after*k*(k+1)//2 + before*k*(k-1)//2)%(10**9+7))