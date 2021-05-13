s = input()
res = 0
B = 0
for i in range(len(s)):
  if s[i] == 'B':
    B += 1
  else:
    res += B
print(res)