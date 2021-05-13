s = str(input())
ss = "CODEFESTIVAL2016"
cou = 0
for i in range(16):
  if s[i] != ss[i]:
    cou += 1
print(cou)