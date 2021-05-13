n, x = map(int,input().split())
l = list(map(int,input().split()))

cnt = 1
now = 0
flg = True
while l:
    now += l.pop(0)
    if now <= x:
        cnt += 1
    else:
      break
print(cnt)