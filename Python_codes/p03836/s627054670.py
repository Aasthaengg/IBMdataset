sx,sy,tx,ty = map(int,input().split())
ans = ''
s1 = (sx,sy+1)
s2 = (sx+1,sy)
s3 = (sx-1,sy)
s4 = (sx,sy-1)
t1 = (tx-1,ty)
t2 = (tx,ty-1)
t3 = (tx,ty+1)
t4 = (tx+1,ty)
l = [s1,t1,s2,t2,s3,t3,s4,t4]
for i in range(4):
    xs,ys = l[i*2]
    xt,yt = l[i*2+1]
    if i%2==0:
        if i == 0:
            ans += 'U'
        else:
            ans += 'L'
        ans += 'U'*(yt-ys)
        ans += 'R'*(xt-xs)
        if i == 0:
            ans += 'R'
        else:
            ans += 'D'
    else:
        if i == 1:
            ans += 'D'
        else:
            ans += 'R'
        ans += 'D'*(yt-ys)
        ans += 'L'*(xt-xs)
        if i == 1:
            ans += 'L'
        else:
            ans += 'U'
    #print(ans)
    #print(yt-ys,xt-xs)
print(ans)
