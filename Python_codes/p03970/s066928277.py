i = input()
truetext = "CODEFESTIVAL2016"
ans = 0
for t in range(len(i)):
  if i[t] != truetext[t]:
    ans += 1
print(ans)