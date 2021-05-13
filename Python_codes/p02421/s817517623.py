c,d=0,0
for i in range(int(input())):
    a,b=map(str,input().split())
    if a>b:
        c+=3
    elif b>a:
        d+=3
    else:
        c+=1
        d+=1
print(c, d)
