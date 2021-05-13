d,g=map(int,input().split())
p=[0]*d
c=[0]*d

ans=10**9
for i in range(d):
    p[i],c[i]=map(int,input().split())
    
for i in range(2**d):
    score=0
    cnt=0
    com=-1
    for j in range(d):
        if ((i >> j) & 1):
            score+=100*(j+1)*p[j]+c[j]
            cnt+=p[j]
        else:
            com=j
 
    flg=0
    if score<g and com>=0:
        while p[com]>flg:
            score+=100*(com+1)
            flg+=1
            if score>=g:
                break
    if score>=g:
        cnt+=flg
        if ans>cnt:
            ans=cnt

print(ans)