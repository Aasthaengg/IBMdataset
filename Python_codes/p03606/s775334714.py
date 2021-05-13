n = int(input())
cnt = 0
for i in range(n):
  l,r = list(map(int, input().split()))
  if(l == r):
    cnt += 1
  else:
    cnt = cnt + r - l + 1
print(cnt)
