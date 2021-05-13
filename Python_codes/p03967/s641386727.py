s = input().strip()
n = len(s)
op = 0
for i in range(n):
  if s[i]=='p':
    op += 1
p = n//2
print(p-op)

