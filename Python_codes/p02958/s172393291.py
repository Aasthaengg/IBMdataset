n = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in range(n):
  if i + 1 != lst[i]:
    cnt += 1
  if cnt >= 3:
    print('NO')
    exit()
print('YES')