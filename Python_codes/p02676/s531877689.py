n = int(input())
s = input()
x = len(s)
if (x <= n):
  print(s)
else:
  for i in range (n):
    print(s[i], end = '')
  print("...")
