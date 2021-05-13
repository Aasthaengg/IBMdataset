n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
f=0
for i in range(n-1):
    if a[i]==a[i+1]:
        f=1
print("YES" if f==0 else "NO")
    
    
        
        
    
    
    
    
        
