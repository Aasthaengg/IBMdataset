line=input().split()
x=int(line[0])
y=int(line[1])
def gcd(x,y):
    r=x%y
    while(r>0):
        x=y
        y=r
        r=x%y
    return y
    
print (gcd(x,y))

