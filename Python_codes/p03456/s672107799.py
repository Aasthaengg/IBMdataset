ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

ab = int(input().replace(' ',''))

for i in range(1000):
  if i**2==ab:
    print('Yes')
    exit()

print('No')
