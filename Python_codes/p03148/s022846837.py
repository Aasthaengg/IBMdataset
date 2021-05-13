import sys
n,k=map(int,input().split())
data=[]
for i in range(n):
    t,d=map(int,input().split())
    data.append([d,t])
data.sort(reverse=True)
flag=[0]*(n+1)
eat=[]
lst=[]
count=0
for u in data:
    d,t=u
    if flag[t]==0:
        eat.append(u)
        flag[t]=1
        count+=1
        if count==k:
            break
    else:
        lst.append(u)
else:
    lst.sort(reverse=True)
    sum=0
    for i in range(n-count):
        if i<k-count:
            sum+=lst[i][0]
        else:
            if lst[i][0]>eat[count-1][0]+2*count-1:
                eat[count-1]=lst[i]
                count-=1
            else:
                break
    for u in eat:
        sum+=u[0]
    sum+=count**2
    print(sum)
    sys.exit()
lst.sort(reverse=True)
for u in lst:
    d=u[0]
    if d>eat[count-1][0]+2*count-1:
        eat[count-1]=u
        count-=1
    else:
        break
sum=0
for u in eat:
    sum+=u[0]
sum+=count**2
print(sum)