n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
b = a[0]
c = []
while True:
  if b == 2:
    print(len(c)+1)
    exit()
  if len(c)> n:
    print(-1)
    exit()
  else:
    c.append(b)
    b = a[c[-1]-1]
