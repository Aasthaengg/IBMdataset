import sys
import math
import itertools as it
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":
    n = I()
    t = Intl()
    m = I()
    px = [Intl() for i in range(m)]
    s = sum(t)
    ps = s
    for i in range(m):
        a,b = px[i][0],px[i][1]
        s -= t[a-1]
        s += b
        print(s)
        s -= b
        s += t[a-1]