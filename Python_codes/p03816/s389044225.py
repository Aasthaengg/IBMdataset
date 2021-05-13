# ABC053 D - Card Eater
from collections import defaultdict
si = lambda: input()
ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))
n=ni()
a=nl()
cnt=0

d=defaultdict(int)
for aa in a:
    d[aa]+=1

for dd in d.items():
    if dd[1]%2==0:
        cnt+=1

if cnt%2==0:
    print(len(set(a)))
else:
    print(len(set(a))-1)