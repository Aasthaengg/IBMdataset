a,b=map(int,input().split())
cnt = 1
ans = 0
while(True):
  if b <= cnt:
    print(ans)
    break
  cnt += a-1
  ans += 1