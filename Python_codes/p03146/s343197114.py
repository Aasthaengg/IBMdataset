s=int(input())
li=[s]
for i in range(10**6):
    if s%2==1:
        s=3*s+1
        li+=[s]
    else:
        s//=2
        li+=[s]
    if len(li)!=len(set(li)):
        print(i+2)
        break