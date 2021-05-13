s = list(input())
n = int(input())
a = ''
for i in range(0, len(s), n):
  a += s[i]
print(a)