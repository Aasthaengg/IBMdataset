n = int(input())
a = list(map(int,input().split()))

#A1 ~ Aiまでの和 O(logN)
def BIT_query(idx):
    res_sum = 0
    while idx > 0:
        res_sum += BIT[idx]
        idx -= idx&(-idx)
    return res_sum

#Ai += x O(logN)
def BIT_update(idx,x):
    while idx <= n:
        BIT[idx] += x
        idx += (idx&(-idx))
    return


BIT = [0]*(n+1)
for i,e in enumerate(a):
   BIT_update(i+1,e)
ans1=0
for i in range(1,n+1):
    SUM=BIT_query(i)
    if i%2==1:
        if SUM<=0:
            ans1+=1-SUM
            BIT_update(i,1-SUM)
    else:
        if SUM>=0:
            ans1+=1+SUM
            BIT_update(i,-1-SUM)


BIT = [0]*(n+1)
for i,e in enumerate(a):
    BIT_update(i+1,e)
ans2=0
for i in range(1,n+1):
    SUM=BIT_query(i)
    if i%2==0:
        if SUM<=0:
            ans2+=1-SUM
            BIT_update(i,1-SUM)
    else:
        if SUM>=0:
            ans2+=1+SUM
            BIT_update(i,-1-SUM)

print(min(ans1,ans2))