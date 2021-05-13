n = int(input())
l = []
for i in range(n):
    a, b = map(int, input().split())
    l.append([a, b])
l = l[::-1]
c = 0
for a, b in l:
  a += c
  if a % b != 0:
    c += b - (a % b)
print(c)