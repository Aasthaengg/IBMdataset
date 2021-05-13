n,m = map(int, input().split())
a = list(map(int, input().split()))

rui=[0]
last=0
for i in range(n):
    last+=a[i]
    rui.append(last)
from collections import defaultdict
mod = defaultdict(int)
for num in rui:
    mod[num%m]+=1

ans=0
for v in mod.values():
    ans+=(v*(v-1))//2
print(ans)