l,r = map(int, input().split())
if l//2019 != r//2019:
  print(0)
  exit(0)
l = l%2019
r = r%2019
a = 2019
for i in range(l,r+1):
  for j in range(l,i):
    a = min(a,(i*j)%2019)
    if a == 0:
      print(0)
      exit(0)
print(a)