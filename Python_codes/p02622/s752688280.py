s = input()
t = input()
n = len(s)
c = 0
for i in range(0,n):
  if s[i] != t[i]:
    c += 1
print(c)