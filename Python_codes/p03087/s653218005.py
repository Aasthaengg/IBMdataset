n,q=map(int,input().split())
s=str(input())
a=[0]
a*=n
for i in range(n-1):
    if s[i]=='A' and s[i+1]=='C':
        a[i+1]=a[i]+1
    else:
        a[i+1]=a[i]
#最初に余分な0が一つ入っているため番号はそのまま        
for i in range(q):
    li,ri=map(int,input().split())
    ans=a[ri-1]-a[li-1]
    print(ans)