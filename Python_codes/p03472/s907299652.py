n,h=map(int,input().split())
a=list()
b=list()
for i in range(n):
    j,k=map(int,input().split())
    a.append(j)
    b.append(k)
#sunb=sum(b)
maxa=max(a)
if maxa>max(b):
    print(-h//maxa*-1)
else:
    b.sort(reverse=True)
    p=0
    for i in range(n):
        p+=b[i]
        if p>=h:
            print(i+1)
            break
        if b[i]<maxa:
            print(i+((p-h-b[i])//maxa)*-1)
            #print(maxa,p)
            break
    else:
        print(n+((p-h)//maxa)*-1)
