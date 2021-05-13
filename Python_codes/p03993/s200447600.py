N=int(input())
a=list(map(int,input().split()))
a.insert(0,0)
ans=0

for i in range(1,len(a)):
  if i==a[a[i]]:
    ans+=1

print(ans//2) 