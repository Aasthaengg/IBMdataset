a,b,t = map(int, input().split())
a_ = a
cnt = 0
while a_<=t+0.5:
    a_ += a
    cnt += b
print(cnt)