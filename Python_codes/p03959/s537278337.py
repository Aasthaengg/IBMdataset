n=int(input())
s=list(map(int,input().split()))
a=list(map(int,input().split()))
uselist=[0 for _ in range(n)]
cnt=0
for i in range(n):
    if cnt!=s[i]:
        cnt=s[i]
        uselist[i]=cnt
    else:
        continue

###
uselist1=[0 for _ in range(n)]
count=0
for i in range(n):
    if count!=a[n-1-i]:
        count=a[n-1-i]
        uselist1[n-1-i]=count
    else:
        continue

###
flag=True
anslist=[0 for _ in range(n)]
for i in range(n):
    if uselist[i]!=0 and uselist1[i]!=0:
        if uselist[i]!=uselist1[i]:
            flag=False
            break
        else:
            anslist[i]=uselist[i]
    elif uselist[i]!=0 and uselist1[i]==0:
        anslist[i]=uselist[i]
    elif uselist[i]==0 and uselist1[i]!=0:
        anslist[i]=uselist1[i]
    else:
        continue
for i in range(n):
    if anslist[n-1-i]>a[n-1-i]:
        flag=False
        break

        
        
ans=1
checker=0
index=0
i=1
if flag:
    anslist.append(0)
    anslist.insert(0,0)
    while i<=n:
        if index==0 and anslist[i]!=0:
            checker=anslist[i]
            i+=1
            
        elif index==0 and anslist[i]==0:
            index+=1
            i+=1
            
        elif index!=0 and anslist[i]!=0:
            checker=min(checker,anslist[i])
            use=1
            for _ in range(index):
                use=(use*checker)%(10**9+7)
            ans=(ans*(use))%(10**9+7)
            checker=anslist[i]
            index=0
            i+=1
        elif index!=0 and anslist[i]==0:
            index+=1
            i+=1
    print(ans%(10**9+7))
if not flag:
    print(0)