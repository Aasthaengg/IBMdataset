s = input()
k = int(input())
if s == '1' * len(s):
  print(1)
  exit()
for i in range(len(s)):
  if s[i] != '1':
    idx = i
    num = s[i]
    break
if idx >= k:
  print(1)
else:
  print(num)