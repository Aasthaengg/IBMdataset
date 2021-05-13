N = int(input())
a = [int(x) for x in input().split()]
alice = 0
bob = 0
a.sort()
i = 0
for x in reversed(a):
  if(i%2==0):
    alice += x
  else:
    bob += x
  i += 1
print(alice-bob)