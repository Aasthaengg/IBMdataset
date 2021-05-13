n = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in lst:
  while i % 2 == 0:
    i //= 2
    cnt += 1
print(cnt)