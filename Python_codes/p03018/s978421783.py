import re

s = input()
ans = 0
s = s.replace("BC", "D")
L = re.split('[BC]', s)
for i in L:
  k = len(i)
  temp = 0
  for j in range(k):
    if i[k-1-j] == "D":
      temp += 1
    else:
      ans += temp
print(ans)