a,b,c=map(int,input().split())
d,e,f=map(int,input().split())
g,h,i=map(int,input().split())
if a+e==b+d:
    if b+f==c+e:
        if d+h==e+g:
            if e+i==f+h:
                print('Yes')
                exit()
print('No')