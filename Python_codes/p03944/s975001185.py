w,h,n=map(int,input().split())
lst=[]
for _ in range(n):
    x,y,a=map(int,input().split())
    if a==1 or a==2:
        lst.append([x,a])
    else:
        lst.append([y,a])
answer=0
for i in range(h):
    for j in range(w):
        ans=True
        for k in range(n):
            nuri,c=lst[k]
            if c==1:
                if j<nuri:
                    ans=False
                    break
            elif c==2:
                if j>=nuri:
                    ans=False
                    break
            elif c==3:
                if i<nuri:
                    ans=False
                    break
            else:
                if i>=nuri:
                    ans=False
                    break
        if ans==True:
            answer+=1
print(answer)