n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

if k != 0:
  del l[-k:]
print(sum(l))
