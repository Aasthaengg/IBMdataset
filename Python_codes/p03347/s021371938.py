n=int(input())
c=[int(input())for i in range(n)]
d=0
p=0
for i in range(n-1,0,-1):
    if c[i]-c[i-1]>1:
        print(-1)
        break
    else:
        if d!=c[i]:
            p+=c[i]
            d=c[i]
    d-=1
else:
    print(-1if c[0]>0else p)