s=input()
n=len(s)
for i in range(1,n//2-1):
    m=n//2-i

    x=s[0] 
    for j in range(m-1):
        x=x+s[j+1]
    y=s[m]
    for j in range(m-1):
        y=y+s[m+1+j]

    if x==y:
        print(2*m)
        exit()
print(2)
        
    
    
