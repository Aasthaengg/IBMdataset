S = input()
ans = 'No'
t = 'C'
for i in range(len(S)):
  if t == 'C' and S[i] == t:
    t = 'F'
  elif t == 'F' and S[i] == t:
    ans = 'Yes'
print(ans)