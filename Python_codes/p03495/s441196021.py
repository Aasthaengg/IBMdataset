from collections import defaultdict
n,k=map(int,input().split())
a=list(map(int,input().split()))
dd=defaultdict(lambda:0)
for aa in a: dd[aa]+=1

diff=len(dd)-k
if diff<=0:
  print(0)
  exit()
l=[x for x in dd.values()]
l.sort()
print(sum(l[:diff]))
