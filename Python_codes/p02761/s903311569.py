n,m=map(int,input().split())
a=[-1 for _ in range(n)]
f=0
if n!=1:
    
    for i in range(m):
        s,c=map(int,input().split())
        if a[s-1]==-1 or a[s-1]==c:
            a[s-1]=c
        if a[s-1]!=-1 and a[s-1]!=c:
            f=1
        if s==1 and c==0:
            f=1
    for q in range(n):
        if q!=0 and a[q]==-1:
            a[q]=0
        if q==0 and a[q]==-1:
            a[q]=1

    ans=0
    for t in range(n):
        ans+=a[n-t-1]*(10**t)
    print(ans if f==0 else -1)
else:
    for i in range(m):
        
        s,c=map(int,input().split())
        if i==0:
            d=c
        if d!=c:
            f=1
            
    if m!=0:
        
        print(c if f==0 else -1)
    if m==0:
        print(0)
        

    
