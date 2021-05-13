N=int(input())
b=list(map(int,input().split()))

tmp=-1
idx=0
count=1
flag=True
ans=[]
while(len(b)):
    #print(idx)
    if idx<len(b):
        if b[idx]==count:
            tmp=idx
            idx+=1
            count+=1
        else:
            idx+=1
            count+=1
    if idx>(len(b)-1):
        if tmp==-1:
            flag=False
            break
        else:
            #print(tmp)
            ans.append(b[tmp])
            del b[tmp]
            tmp=-1
            idx=0
            count=1
#print(ans)
if flag:
    for i in range(len(ans)):
        print(ans[len(ans)-1-i])
else:
    print(-1)