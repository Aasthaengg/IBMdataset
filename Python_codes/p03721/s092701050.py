import sys

n, k = map(int, input().split())
element = [None]*n

for i in range(n):
  element[i] = [int(x) for x in input().split()]

element.sort()

c = 0
for i in range(n):
  c += element[i][1]
  if c >= k:
    print(element[i][0])
    sys.exit()