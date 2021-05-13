s = input()
t = input()

ans = 0
for s_i, t_i in zip(s,t):
  if s_i == t_i:
    ans += 1

print(ans)