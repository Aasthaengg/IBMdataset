L,R = map(int,input().split())
if(R-L<2019):    
    L = L%2019 
    R = R%2019
    ans = float('inf')
    for i in range(min(L,R),max(L,R)+1):
        for j in range(i+1,max(L,R)+1):
            ans=min(ans,(i*j)%2019)
    print(ans)
else:
    print(0)