n = int(input())
cnt = 0
for i in range(n+1):
  s = len(str(i))
  if s % 2 == 1:
    cnt += 1

print(cnt-1)