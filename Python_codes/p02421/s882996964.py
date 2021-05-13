n=int(input())

t=0
h=0

for i in range(n):
    T,H=map(str,input().split())
    
    if T>H:
        t+=3
    elif T<H:
        h+=3
    else:
        t+=1
        h+=1
        
print(t,h)
