n = int(input())
d, x = map(int, input().split())
c = 0
for i in range(n):
  c += len(range(1, d+1, int(input())))
print(c+x)