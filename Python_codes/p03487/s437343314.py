from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))

dd=defaultdict(lambda:0)
for aa in a: dd[aa]+=1

ans=0
for aa in dd.keys():
  ca=dd[aa]
  if ca>=aa:
    ans+=ca-aa
  else:
    ans+=ca
print(ans)