p = []
for i in range(3):
  a, b = input().split()
  p.append(a)
  p.append(b)

if sorted(p) == ['1','2','2','3','3','4']:
  print("YES")
else:
  print("NO")