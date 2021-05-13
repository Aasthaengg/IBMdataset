x=int(input())
if x == 0 or x == 1 : print("1")
else : 
    i=0
    b=1
    c=1
    while i<(x-1) :
        d=b+c
        c=b
        b=d
        i=i+1
        
    print(b)
        
