H, W, N = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]

from itertools import product

S = [set() for _ in range(10)]
# S[i]: set(黒いマスをi個こ含む3*3マスの中心セル)

memo = {}
for a,b in AB:
  for x,y in product([-1,0,1], repeat=2):
    X = a+x-1
    Y = b+y-1
    if X<=0 or H-1<=X or Y<=0 or W-1<=Y:
      continue
    memo[(X,Y)] = memo.get((X,Y),0) + 1

#print(memo)

from collections import Counter
c = Counter(memo.values())
L = [c.get(i,0) for i in range(1,10)]

print((H-2)*(W-2) - sum(L))

for l in L:
  print(l)