S = input()
ans = 0
for i in range(len(S)):
  for j in range(i, len(S)):
    if all('ACTG'.count(c) == 1 for c in S[i:j+1]):
      ans = max(ans, j+1-i)
print(ans)