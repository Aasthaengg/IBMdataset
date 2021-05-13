n=int(input(""))
le=len(str(n))
ten=10**(le-1)
one=int(str(n)[-1])

b=[]
for k in range(9):
    a=[]
    for i in range(9):
        a+=[0]
    b+=[a]
    
if(le==1):
    print(1)
else:
    
    for i in range(9):
            s=0
            if(ten*(i+2)<=n):
                s=10**(le-2)
                for k in range(9):
                    b[i][k]+=s
            elif(ten*(i+1)<n):
                s=int((n-ten*(i+1))/10)+1
                if(one==0):
                    s-=1
                for k in range(9):
                    
                    b[i][k]+=s
                    if (k+1==one):
                        s-=1
    
    for i in range(9):
        b[i][i]=1+b[i][i]
        
    s=0    
    for i in range(2,le):
            s+=10**(i-2)
    
    c=0
    for i in range(9):
        for k in range(9):
            c+=(b[i][k]+s)*(b[k][i]+s)
    
            
        
        
    print(c)
                
                
                
            
