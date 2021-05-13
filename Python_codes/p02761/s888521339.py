n,m = map(int,input().split())

A = [-1]*n

ans = 0
is_kaburi = 0
for i in range(m):
    
    s,c = map(int,input().split())
    
    if A[s-1] == -1 or A[s-1] == c:
        A[s-1] = c
          
    else:

        is_kaburi=1


if is_kaburi==1:
    print(-1)    

else:
    if n>1 and A[0] == -1:
        A[0] = 1
        
    elif n==1 and A[0] == -1:
        A[0] = 0
        
    if n != 1 and A[0] == 0:
        print(-1)
        
    else:
        
        for i in range(n):
            
            if A[i] == -1:
                A[i] = 0
                
            ans = ans*10 +A[i]
        
        print(ans)