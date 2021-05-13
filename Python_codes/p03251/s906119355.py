"""MILOY"""
n,m,x,y=list(map(int,input().split()))
line1=list(map(int,input().split()))
line2=list(map(int,input().split()))
t=0
try:
    for i in range(x+1,y+1):
        c=0
        s=0
        for j in line1:
            if (i<=j):
                c+=1
            
        for j in line2:
            if(i>j):
                s+=1
              
        if ( c==0 and s==0):
            t=t+1
           
    
    if(t==0):
        print('War')
    if(t!=0):
        print('No War')
        
except:
    print('War')
