xlist = list(map(int,input().split()))
cnt = 0
for i in xlist:
    cnt += 1
    if i == 0:
        print(cnt)