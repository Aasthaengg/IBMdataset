n = int(input())
a,b = [],[]
for i in range(n):
  aa, bb = map(int, input().split())
  a.append(aa)
  b.append(bb)

print (max(a)+min(b))