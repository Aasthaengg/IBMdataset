import math

for i in range(50):
    
    m,f,r=list(map(float, input().split()))
    x=m+f
    if m==-1 and f==-1 and r==-1:
        break
    
    elif m==-1 or f==-1 :
        print("F")
        
    elif x>=80 :
        print("A")
    
    elif 80>x>=65 :
        print("B")
    
    elif 65>x>=50 :
        print("C")
        
    elif 50>x>=30 :
        if r>=50 :
            print("C")
        else :
            print("D")
    else :
        print("F")
