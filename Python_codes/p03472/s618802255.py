n,h= map(int, input().split())
a = 0
num = 0
b = []
for i in range(n):
  c,d = map(int, input().split())
  if c > a:
    a = c
    num = i
  b.append(d)
cnt = 0
b2 = b[num]
b = sorted(b)
if a >= max(b):
  if h%a == 0:
    print(h//a)
  else:
    print(h//a + 1)
  exit(0)
  
for i,j in enumerate(b):
  if j > a:
    b = sorted(b[i:], reverse=True)
    break
for i in b:
  h -= i
  cnt += 1
  if h <= 0:
    print(cnt)
    exit(0)
if h%a == 0:
  print(cnt + h//a)
else:
  print(cnt + h//a + 1)