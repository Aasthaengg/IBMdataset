import itertools
n, a, b, c =map(int, input().split())
ans = float("inf")
take = [int(input()) for i in range(n)]

for pattern in itertools.product(range(4), repeat=n):
    abc = [0]*3
    mp=0
    for i in range(n):
      if pattern[i]==3:
        continue
      else:
        if abc[pattern[i]] != 0:
          mp+=10
        abc[pattern[i]]+=take[i]
    
    mp+=abs(a-abc[0])
    mp+=abs(b-abc[1])
    mp+=abs(c-abc[2])
    for i in range(3):
      if abc[i]==0:
        mp=float("inf")
        break
    ans = min(ans, mp)
    
print(ans)
