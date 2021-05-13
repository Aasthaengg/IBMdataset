n = int(input())
s = input()
if (n%2 == 1):
  print("No")
else:
  c = 0
  for i in range(int(n/2)):
    if (s[i] != s[i + int(n/2)]):
      c = 1
  if (c == 0):
    print("Yes")
  else:
    print("No")