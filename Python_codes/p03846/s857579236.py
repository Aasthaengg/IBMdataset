n=int(input())
a=list(map(int, input().split()))
mod=10**9+7

from collections import Counter
c=Counter(a)

cnt_lst=[0]*n
for key in c:
    cnt_lst[key]+=c[key]

flag=True
if n%2==1:
    if cnt_lst[0]==1:
        cnt_lst.pop(0)
    else:
        flag=False
    for i in range(n-1):
        if (i%2==1 and cnt_lst[i]!=2) or (i%2==0 and cnt_lst[i]!=0):
            flag=False
else:
    for i in range(n):
        if (i%2==1 and cnt_lst[i]!=2) or (i%2==0 and cnt_lst[i]!=0):
            flag=False

print(2**(n//2)%mod if flag else 0)