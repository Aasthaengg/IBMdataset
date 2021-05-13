n = int(input())
l = list(map(int,input().split()))
cnt = 0
for v in l:
  if v % 2 != 0:
    cnt += 1
print('YES' if cnt % 2 == 0 else 'NO')