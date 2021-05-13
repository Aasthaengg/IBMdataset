def resolve():
    b,c =map(int,input().split())
    if b==1:print(c)
    else:
        print(c*pow(c-1,b-1))
    
        
#%%submit!
resolve()