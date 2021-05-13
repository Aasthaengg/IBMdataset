n = int(input())
s = input()
t = ""
for i in s:
  a = ord(i) + n
  if a > ord("Z"):
    a = a - 26
  t += chr(a)
print(t)