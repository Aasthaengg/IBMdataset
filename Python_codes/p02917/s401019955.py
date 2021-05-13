n=int(input())
bb=list(map(int,input().split()))
aa=[0]*n
aa[0]=bb[0]
for i in range(n-1):
  aa[i]=min(aa[i],bb[i])
  aa[i+1]=max(aa[i+1],bb[i])
print(sum(aa))
