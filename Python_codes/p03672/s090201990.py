S = input()
ans = 0
i = 1
while i * 2 < len(S):
  l = S[:i]
  r = S[i:i*2]
  if(l == r):
    ans = i * 2
  i += 1
print(ans)