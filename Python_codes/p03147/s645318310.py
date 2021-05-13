n=int(input())
h=list(map(int,input().split()))
if n==1:
    print(h[0])
elif n==2:
    print(max(h))
else:
    h.append(0)
    h.insert(0,0)
    
    ans=0
    f=[0 for i in range(n+2)]
    
    for i in range(10010):
        a=1
        x=[]
        for j in range(n+2):
            if h[j]<=f[j]:
                x.append(j)
        m=len(x)
        if m==n+2:
            break
        a=m-1
        for j in range(m-1):
            if x[j]+1==x[j+1]:
                a-=1
        ans+=a
        for j in range(n+2):
            f[j]+=1
        
    print(ans)
            
            
            
            
        
    
        
        
        
          
