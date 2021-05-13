S = input().strip()
ans = 0
for c1,c2 in zip(S,'CODEFESTIVAL2016'):
  if c1 != c2:
    ans += 1
print(ans)