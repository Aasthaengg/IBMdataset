n=int(input())
a=list(map(int,input().split()))
ans=1
if n==1:
    print(ans)
    exit()
c=0#1なら増加傾向、2なら減少傾向
for i in range(n):
    if i!=n-1:
        if c==1:
            if a[i+1]<a[i]:
                ans+=1
                c=0
                continue
        elif c==2:
            if a[i+1]>a[i]:
                ans+=1
                c=0
                continue
        
        if a[i+1]>a[i]:
            c=1
        elif a[i+1]<a[i]:
            c=2
print(ans)