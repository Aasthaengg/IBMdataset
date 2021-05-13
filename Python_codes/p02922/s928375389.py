A, B = map(int, input().split())

cnt = 1
for i in range(30):
  if cnt >= B:
    break
  cnt += A - 1

print(i)
