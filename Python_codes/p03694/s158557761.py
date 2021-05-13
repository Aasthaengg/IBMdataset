n=int(input())
aa=list(map(int,input().split()))
aa.sort()
d=0
for i in range(1,len(aa)):
  d+=abs(aa[i]-aa[i-1])
print(d)