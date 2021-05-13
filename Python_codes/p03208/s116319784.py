n,k=map(int,input().split())
h=[]
for i in range(n):
    h.append(int(input()))
h=sorted(h)
ans=10**10
for i in range(n-k+1):
    ans=min(ans,h[k-1+i]-h[i])
print(ans)
    
    
            
            
        
    
        
        
        
          
