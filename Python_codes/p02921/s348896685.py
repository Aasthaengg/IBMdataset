args = [input() for _ in range(2)]

S = args[0]
T = args[1]

ans = 0
for s, t in zip(S, T):
  ans += (s == t)
  
print(ans)