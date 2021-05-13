n = int(input())
a = [int(x.strip()) for x in input().split()]
a = sorted(a, reverse=True)
alice,bob = 0,0
for i in range(n):
  if i % 2 == 0:
    alice += a[i]
  else:
    bob += a[i]
print(alice-bob)