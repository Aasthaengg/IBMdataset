n=int(input())
a=list(map(int,input().split()))
l=[0]*n
for i in range(n):
  cnt=0
  while a[i]%2==0:
    a[i]/=2
    cnt+=1
  l[i]+=cnt
print(min(l))