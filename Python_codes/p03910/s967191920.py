n = int(input())
def ok(x):
    return x*(x+1)//2 >= n
for x in range(1,n+1):
    
    if ok(x):
        ans = []
        v = x*(x+1)//2 - n
        
        for i in range(1,x+1):
            if i == v:continue
            
            ans.append(i)
        break
            
        
        
        
    else:continue
print(*ans)