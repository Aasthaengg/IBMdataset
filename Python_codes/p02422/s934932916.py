a=input()
a=list(a)
b=int(input())
c=[]
for i in range(b):
    c.append(input().split())
    x=int(c[i][1])
    y=int(c[i][2])
    if c[i][0]=="replace":
        a[x:y+1]=c[i][3]
    elif c[i][0]=="reverse":
        z=a[x:y+1]
        z.reverse()
        a[x:y+1]=z
    else:
        w=a[x:y+1]
        print("".join(w))
