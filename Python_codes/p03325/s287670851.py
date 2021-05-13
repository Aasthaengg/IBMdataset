N = int(input())
a = list(map(int, input().split()))

cnt = 0
tmp = 0

for i in range(N):
  if a[i]%2 == 0:
    while a[i]%(2**tmp) ==0:
      tmp = tmp + 1
    cnt = cnt + tmp -1
    tmp = 0
print(cnt)