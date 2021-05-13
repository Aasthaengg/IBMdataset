N,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
cnt = 0
for elem in a:
  if x >= elem:
    cnt += 1
    x -= elem
  else:
    break
print(cnt if cnt != N or x == 0 else cnt - 1)
