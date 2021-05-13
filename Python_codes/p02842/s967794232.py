ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

from math import floor

n=ni()

for i in range(n+1):
  if floor(i*1.08)==n:
    print(i)
    exit()
print(':(')
