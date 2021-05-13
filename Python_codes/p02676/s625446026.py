k = int(input())
s = input()
l = len(s)
if k >= l:
  print(s)
else:
  print(s[0:k] + "...")