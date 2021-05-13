s = input()

length = 0
if len(s) % 2 == 0:
  length = len(s) // 2 - 1
else:
  length = len(s) // 2

top = -1

for i in range(length):
  flag = True
  for j in range(i):
    if s[j] != s[i + j + 1]:
      flag = False
  if flag :
    top = (i+1) * 2

print(top)
