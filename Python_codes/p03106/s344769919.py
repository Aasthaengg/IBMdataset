a, b, k = map(int, input().split())
cnt = 0
for i in range(110):
  j = 110 - i
  if a % j == 0 and b % j == 0:
    cnt += 1
  if cnt == k:
    print(j)
    exit()