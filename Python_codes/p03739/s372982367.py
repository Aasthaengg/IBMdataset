n  = int(input())
A = list(map(int,input().split()))
pal = [-1,1]
cnt = 10**18
for p in pal:
    s = 0
    tmp = 0
    prev = p
    for a in A:
        s+=a
        if s==0:
            tmp+=1
            s = prev
            prev*=-1
            continue
        if a==0:
            tmp +=abs(s)+1
            s = prev
            prev*=-1
            continue
        if s//abs(s) != prev:
            tmp+=abs(s)+1
            s = prev
        else:
            pass
        prev*=-1
    cnt = min(cnt,tmp)
print(cnt)
