S = "CODEFESTIVAL2016"
s = input()
result = 0
for i in range(16):
  if S[i] != s[i]:
    result += 1
print(result)
