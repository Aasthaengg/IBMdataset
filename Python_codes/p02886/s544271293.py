import itertools
n = int(input())
a = list(map(int,input().split()))
cnt = 0
for i, j in itertools.combinations(a, 2):
  cnt += i*j
print(cnt)