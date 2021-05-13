def inp():return map(int,input().split())
a,b=inp()
for x in range(b-a+1,b+a):
    print(x,end=" ")