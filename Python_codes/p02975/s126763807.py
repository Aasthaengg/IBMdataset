from collections import Counter
n=int(input())
a=list(map(int,input().split()))
flg=False
if all(a[i]==0 for i in range(n)):flg=True
if n%3==0:
    l=Counter(a)
    ans=l.most_common()
    if len(ans)==2:
        flg1,flg2=False,False
        for i,j in ans:
            if i==0 and n%j==0 and n//j==3:
                flg1=True
            if j/n==2/3:
                flg2=True
            if flg1 and flg2:
                flg=True
    if len(ans)==3:
        flg3=True
        tmp=0
        for i in range(3):
            tmp^=ans[i][0]
            if ans[i][1]*3!=n:
                flg3=False
            if flg3 and tmp==0:
                flg=True
if flg:
    print("Yes")
else:
    print("No")