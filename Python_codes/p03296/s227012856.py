N = int(input())
A = list(map(int, input().split()))
cl = 0
c = 0
for a in A:
  if cl != a:
    cl = a
  else:
    cl = 0
    c += 1
print(c)