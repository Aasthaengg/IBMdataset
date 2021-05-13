n = int(input())
P = list(map(int,input().split()))
P = [int(i+1==P[i]) for i in range(n)]+[0]

ans = 0
ex = 0
for p in P:
  if p and ex:
    ans += 1
    ex = 0
  elif p:
    ex = 1
  elif ex:
    ans += 1
    ex = 0
print(ans)

