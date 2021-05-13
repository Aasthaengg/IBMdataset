N = int(input())
a = [int(input()) for i in range(N)]
cnt = 1
jumpto = a[0]
if jumpto==2:
  print(cnt)
  exit()
for i in range(N):
  jumpto = a[jumpto-1]
  cnt += 1
  if jumpto ==2:
    print(cnt)
    exit()
print(-1)
