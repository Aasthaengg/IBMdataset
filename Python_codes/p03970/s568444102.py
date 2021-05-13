s = "CODEFESTIVAL2016"
t = list(input())
count = 0
for i in range(16):
  if s[i]!=t[i]:
    count += 1
print(count)