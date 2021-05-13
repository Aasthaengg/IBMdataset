n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

for i in range(n - 2):
  if all([d[i + j][0] == d[i + j][1] for j in range(3)]):
    print('Yes')
    exit()

print('No')
