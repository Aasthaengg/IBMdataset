n = int(input())
l = []
for i in range(n):
  l.append(int(input()))
h = max(l)
l.remove(h)
print(sum(l)+h//2)