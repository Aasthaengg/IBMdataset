n=int(input())
ar=[]
def g(i):
    return i[2]
for _ in range(n):
    a,b,c=map(int,input().strip().split(" "))
    ar.append((a,b,c))
ar.sort(key=g,reverse=True)

for x in range(101):
    for y in range(101):
        t=1
        p=(x,y)
        h=0
        for i in range(n):
            if h==0:
                h=ar[i][2]+abs(ar[i][0]-x)+abs(ar[i][1]-y)
            elif ar[i][2]>0:
                c_h=ar[i][2]+abs(ar[i][0]-x)+abs(ar[i][1]-y)
                if c_h!=h:
                    t=0
                    break
            else:
                if h-(abs(ar[i][0]-x)+abs(ar[i][1]-y))>0:
                    t=0
                    break
        if t==1:
            ans=(x,y,h)
            break
for i in ans:
    print(i,end=" ")
