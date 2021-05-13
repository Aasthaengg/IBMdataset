S = input()
ans = "No"
for i in range(len(S)):
  if S[i] == "7":
    ans = "Yes"
    break
print(ans)