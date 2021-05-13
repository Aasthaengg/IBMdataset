n=int(input())
a=100000
while n!=0:
    a=a*1.05
    if a%1000!=0:
        a=a-(a%1000)+1000
    
    
    n=n-1
print(int (a))

