n,m,x,y=map(int,input().split())
X=list(map(int,input().split()))
Y=list(map(int,input().split()))
mx=max(X)
my=min(Y)
if mx<my:
    for i in range(mx+1,my+1):
        if x<i<=y:
            print("No War")
            exit()
    print("War")
    
        
    

else:
    print("War")


            
