a = input().split()
N = int(a[1])
mini = []
maxi = []

for i in range(N):
  b = input().split()
  mini.append(b[0])
  maxi.append(b[1])
  
c = [int(s) for s in mini]
d = [int(s) for s in maxi]

c = sorted(c)
d = sorted(d, reverse=True)
e = min(d) - max(c)

if e >= 0:
  print(e + 1)
else:
  print(0)