S = input()
W = []
 
for i, s in enumerate(S):
  if s == 'W':
    W.append(i)

idx = 0
ans = 0
for w in W:
  ans += w-idx
  idx += 1

print(ans)