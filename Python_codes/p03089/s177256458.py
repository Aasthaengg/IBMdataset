n=int(input())
b=list(map(int,input().split()))
ans=[]
for i in range(n):
    t=1
    tmp=0
    for j in range(len(b)):
        if b[t-1]==t:
            tmp=t
        t+=1
    if tmp==0:
        print(-1)
        exit()
    else:
        ans.append(b.pop(tmp-1))
        
if b:
    print(-1)
else:
    print(*ans[::-1])