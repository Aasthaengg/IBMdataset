
x=int(input())
list=[]
c=0
d=0
for i in range(x):
    a,b=input().split()
    
    if a<b:
        d+=3
    elif a>b:
        c+=3
    else:
        c+=1
        d+=1
print(c,d)
