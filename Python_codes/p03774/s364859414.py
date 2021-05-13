N,M = map(int,input().split())

a=[0]*N
b=[0]*N
c=[0]*M
d=[0]*M


for i in range(N):
    a[i],b[i] = map(int,input().split())
    
    
for i in range(M):
    c[i],d[i] = map(int,input().split())
    
    
for i in range(N):
    x = a[i]
    y = b[i]
    
    for j in range(M):
        
        cx = c[j]
        cy = d[j]
        
        temp = abs(cx-x) + abs(cy-y)
        
        if j==0:
            Min = temp
            result =1
        elif Min > temp:
            result = j+1
            Min = temp
            
            
    print(result)