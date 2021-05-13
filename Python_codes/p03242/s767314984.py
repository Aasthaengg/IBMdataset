S = ""
ans = ""
S = input()
for i in range(3):
  if S[i] == "1":
    ans += "9"
  elif S[i] == "9":
    ans += "1"
  else:
    ans += S[i]
print(ans)