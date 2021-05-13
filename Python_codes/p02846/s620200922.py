t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
import time
start=time.time()
x=(a1-b1)*t1
y=(a2-b2)*t2
if x<0:
    if x+y<0:
        print(0)
        exit()
    if x+y==0:
        print("infinity")
        exit()
    if -1*x%(x+y):
        print(-1*x//(x+y)*2+1)
    else:
        print(-1*x//(x+y)*2)
else:
    x*=-1
    y*=-1
    if x+y<0:
        print(0)
        exit()
    if x+y==0:
        print("infinity")
        exit()
    if -1*x%(x+y):
        print(-1*x//(x+y)*2+1)
    else:
        print(-1*x//(x+y)*2)
