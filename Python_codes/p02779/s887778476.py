from collections import defaultdict
dic = defaultdict(int)

N = int(input())
for a in list(map(int, input().split())):
  dic[a] += 1
  if dic[a] >= 2:
    print('NO')
    exit()
print('YES')