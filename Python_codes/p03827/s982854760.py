n = int(input())
s = input()
temp = 0
res = 0
for i in range(n):
  if s[i] == 'I':
    temp += 1
  else:
    temp -= 1
  res = max(res, temp)
print(res)