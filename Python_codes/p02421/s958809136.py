n=int(input())
T=0
H=0
for i in range(n):
    t,h=input().split()
    if t==h:
        T+=1
        H+=1
    else:
        if t>h:
            T+=3
        else:
            H+=3
    
print(T,H)
