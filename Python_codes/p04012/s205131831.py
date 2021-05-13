s = input()
alphabets = [0] * 26
for i in range(len(s)):
  a = ord(s[i])
  alphabets[a-97] += 1
flag = True
for x in alphabets:
  if x % 2 != 0:
    flag = False
if flag:
  print('Yes')
else:
  print('No')