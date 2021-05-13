h,a=map(int,input().split())
cnt = 0
while True:
    if h > 0:
        h -= a
        cnt += 1
    else:
        break
print(cnt)
