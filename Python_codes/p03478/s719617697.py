a ,b ,c = input().split()

ans = 0

for i in range( 1 , int(a)+1 ):
    
    o = str(i)
    
    count = 0
    
    for k in range( 0 , len(o)) :
        
        count += int(o[k])
    
    if count >= int(b) and count <= int(c):
        
        ans += i
        
print(ans)
