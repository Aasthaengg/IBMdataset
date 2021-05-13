n = int(input())
s = input()
t = input()
a = n
if s == t:
  a = 0
else:
  for i in range(n):
    if s[i:] == t[:-i]:
      a = i
      break
print(a+n)