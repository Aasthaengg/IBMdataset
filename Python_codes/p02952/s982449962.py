n = int(input())
cnt = 0
for i in range(1,n+1):
  if i // 10 == 0 or 10 <= i//10 < 100 or 1000 <= i//10 < 10000:
    cnt += 1
print(cnt)