H, W, N = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]

from itertools import product

# S = [set() for _ in range(10)]
# S[i]: set(黒いマスをi個こ含む3*3マスの中心セル)

memo = {}
ans = [0]*10

P = list(product([-1,0,1], repeat=2))

for a,b in AB:
  for x,y in P:
    X = a+x-1
    Y = b+y-1
    #print(a,b,x,y,X,Y, ans)
    if X<=0 or H-1<=X or Y<=0 or W-1<=Y:
      continue
    memo[(X,Y)] = memo.get((X,Y),0) + 1
    ans[memo[(X,Y)]] += 1
    ans[memo[(X,Y)]-1] -= 1
    
#print(memo)

print((H-2)*(W-2) - sum(ans[1:]))

for n in ans[1:]:
  print(n)