n=int(input())
a=[int(input()) for i in range(n)]
cnt=0
for i in range(n):
    cnt+=1
    if i==0:
        osu=1
        hikaru=a[0]
    else:
        osu=hikaru
        hikaru=a[osu-1]
    if hikaru==2:
        print(cnt)
        break
else:
    print(-1)