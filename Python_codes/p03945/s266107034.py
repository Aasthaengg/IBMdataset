S = list(input())
prev = S[0]
L = len(S)
ans = 0
for i in range(1,L):
  s = S[i]
  if prev != s:
    ans += 1
    prev = s
print(ans)