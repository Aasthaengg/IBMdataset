import sys

n = int(input())
p = list(map(int, input().split()))

pp = [i for i in range(1, n+1)]
cnt = 0

for i in range(n):
  if p[i] != pp[i]:
    cnt += 1
  if cnt > 2:
    print('NO')
    sys.exit()

print('YES')