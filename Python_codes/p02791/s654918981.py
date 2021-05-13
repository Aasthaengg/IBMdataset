n = int(input())
p = [int(i) for i in input().split()]
cnt = 0
min_ = float('inf')
for pi in p:
  if pi < min_:
    cnt += 1
    min_ = pi
print(cnt)