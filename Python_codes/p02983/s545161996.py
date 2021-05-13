l,r = map(int,input().split())
 
x = []
 
if r-l >4038:
    print(0)
else:
    for i in range(l,r+1):
        x.append(i%2019)
        
    x.sort()
    
    ans = x[0]*x[1]%2019
    
    x = list(set(x))
    
    for s in range(len(x)):
        for t in range(s+1,len(x)):
            ans = min(ans,x[s]*x[t]%2019)
        
    print(ans)