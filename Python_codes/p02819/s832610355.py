
x=int(input())
p=[1 for i in range(100010)]
for i in range(2,100011):
    k=2*i
    while k<=100009:
        p[k]=0
        k+=i
z=x
f=0
while f==0:
    if p[z]==1:
        print(z)
        f=1
    z+=1

    
    


    
        
        
    
    
    
    
        
