n=int(input())
a = list(map(int,input().split()))
t = 0
for aa in a:
  t = t ^ aa

r = []
for aa in a:
  r.append(t ^ aa)
print(*r, sep=' ')