S = input()
ans = "NO"
for i in range(len(S)):
  for j in range(len(S)):
    if S[0:i] + S[i+j:len(S)] == "keyence":
      print("YES")
      exit()
print(ans)