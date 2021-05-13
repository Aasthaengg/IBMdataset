n = int(input())
xa = 0
by = 0
ba = 0
counter = 0
for _ in range(n):
  s = input()
  counter += s.count('AB')
  if s[0]=='B':
    if s[-1]=='A':
      ba += 1
    else:
      by += 1
  elif s[-1] == 'A':
    xa += 1
if ba == 0:
  counter += min(xa,by)
else:
  if xa+by== 0:
    counter += ba -1
  else:
    counter += ba + min(xa,by)
print(counter)