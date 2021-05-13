n,x = map(int,input().split())
bound = list(map(int,input().split()))
cnt = 1
pos = 0
for i in range(n):
  pos += bound[i]
  if pos <= x:
    cnt += 1
  if pos > x:
    break
print(cnt)