pt,ph=0,0
for i in range(int(input())):
    t,h=input().split()
    if t>h:
        pt+=3
    elif t==h:
        pt+=1
        ph+=1
    else:
        ph+=3
print(*[pt,ph]) 
