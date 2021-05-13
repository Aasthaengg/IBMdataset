from collections import Counter
n=int(input())
aa=list(map(int,input().split()))
a=Counter(aa)
aa=sum(aa)
aaa=[]
q=int(input())
for i in range(q):
  b,c=map(int,input().split())
  aa+=(c-b)*a[b]
  if c in a.keys():
    a[c]+=a[b]
  else:
    a[c]=a[b]
  a[b]=0
  aaa.append(str(aa))
print('\n'.join(aaa))