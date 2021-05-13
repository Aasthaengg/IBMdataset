import sys
import math
import itertools as it
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

def f(x1,y1,x2,y2,t):
    l = abs(x1-x2)+abs(y1-y2)
    if l <= t:
        if l%2 == t%2:
            return True
    return False

if __name__ == "__main__":
    n = I()
    t = [0]
    x = [0]
    y = [0]
    for i in range(n):
        a,b,c = I2()
        t.append(a)
        x.append(b)
        y.append(c)
    for i in range(n):
        #print(x[i],y[i],x[i+1],y[i+1],t[i+1]-t[i])
        if not f(x[i],y[i],x[i+1],y[i+1],t[i+1]-t[i]):
            print("No")
            exit()
    print("Yes")