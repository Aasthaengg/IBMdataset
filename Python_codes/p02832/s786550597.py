n = int(input())
a = list(map(int,input().split()))

cnt = 0
num = 1
for i in range(n):
  if a[i] == num :
    num += 1
    continue
  cnt += 1

print(cnt if num > 1 else -1)
