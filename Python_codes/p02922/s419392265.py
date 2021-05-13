a,b = map(int,input().split())
cnt = 1
c = b-a
if c >0:
    cnt += (c//(a-1))
    d = c%(a-1)
    if d != 0:
        cnt += 1
if b == 1:
    cnt = 0
print(cnt)