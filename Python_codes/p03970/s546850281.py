s = input()
S = "CODEFESTIVAL2016"
ans = 0
for a,b in zip(s,S):
  if a != b:
    ans += 1
print(ans)