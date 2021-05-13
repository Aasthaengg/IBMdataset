n, x = map(int, input().split())
lst = [0] + list(map(int, input().split()))
cnt = 0
for i in range(n + 1):
  cnt += lst[i]
  if cnt > x:
    print(i)
    exit()
print(n + 1)