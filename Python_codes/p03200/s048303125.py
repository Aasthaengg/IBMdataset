S = input()
b = "B"
w = "W"
con = 0
ans = 0
for i in range(len(S)):
  if S[i] == b:
    con += 1
  elif S[i] == w:
    ans += con
print(ans)