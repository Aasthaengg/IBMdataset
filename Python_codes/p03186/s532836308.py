a,b,c=[int(i) for i in input().split()]
cnt=0
if c<=b:
    cnt=b+c
else:
    cnt+=min(b,c)*2
    c-=b
    if c>0:
        cnt+=min(a,c)
        c-=a
        if c>0:
            cnt+=1

print(cnt)