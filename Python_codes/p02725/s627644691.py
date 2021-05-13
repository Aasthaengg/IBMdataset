k,n = map(int,input().split()) 
A=list(map(int,input().split()) )
ans=10**10
for i in range(len(A)):
    
    #時計回り　iからi-1に行く
    #0を超えない
    if A[i-1] - A[i] > 0:    
        dist1  = A[i-1] - A[i]    
    
    #0を超える
    else:
        dist1 = A[i-1] + (k-A[i])
    
        
    #反時計回り　i-1からiに行く
    
    if A[i] - A[i-1] < 0:    
        dist2  = A[i-1] - A[i]    
    
    #0を超える
    else:
        
        dist2 = A[i] + (k-A[i-1])
        
    dist = min(dist1,dist2)
    
    ans = min(ans,dist)

print(ans)   