n=int(input())
h=list(map(int,input().split()))

cnt=0

while 1:
    for i in range(len(h)-1,0,-1):
        if h[i]==h[i-1]:
            h.pop(i)

    if len(h)==1:
        break
    # mp:水やりポイント
    mp = h.index(max(h))

    if mp==0:
        cnt += h[mp] - h[mp+1]
    elif mp==len(h)-1:
        cnt += h[mp] - h[mp-1]
    else:
        cnt += h[mp] - max(h[mp-1],h[mp+1])

    h.pop(mp)

print(cnt+h[0])
