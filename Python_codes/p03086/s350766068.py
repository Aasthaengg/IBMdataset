S = input()
ans = 0
c = 0
for i in range(len(S)):
  if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
    c += 1
    ans = max(ans, c)
  else:
    c = 0
print(ans)