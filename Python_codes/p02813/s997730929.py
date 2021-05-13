from itertools import permutations
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

t = 0
x = 0
y = 0
for i in permutations(range(1,n+1), n):
  t += 1
  if i == p: x = t
  if i == q: y = t
print(abs(x-y))