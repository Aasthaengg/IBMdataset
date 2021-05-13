import itertools
def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
ans=0
N=II()
L=LI()
c = itertools.combinations(L, 3)
for v in itertools.combinations(L, 3):
    v=list(v)
    v.sort()
    if v[0]==v[1] or v[1]==v[2]:
      continue
    if v[0]+v[1]>v[2]:
      ans+=1
print(ans)