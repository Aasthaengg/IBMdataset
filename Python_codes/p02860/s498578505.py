n = int(input())
s = input()
h = int(n/2)

if (n % 2 == 0) and (s[:h] == s[h:]):
  print("Yes")
else:
  print("No")