
x=int(input())
m=1
if x<=3:
    print(1)
else:
    for p in range(2,12):
        a=2
        while a**p<=x:
            m=max(m,a**p)
            a+=1
    print(m)
        
        
