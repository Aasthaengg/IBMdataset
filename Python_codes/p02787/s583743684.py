import sys
sys.setrecursionlimit(10**5)

h,n=map(int,input().split())
magic=[]
for i in range(n):
  magic.append(tuple(map(int,input().split())))

memo={}
def d(hp):
  if hp<=0:
    return 0
  if hp in memo:
    return memo[hp]
  mn=10**10
  for i in magic:
    mn=min(mn,d(hp-i[0])+i[1])
  memo[hp]=mn
  return mn

for i in range(1,h-1):
  d(i)
print(d(h))