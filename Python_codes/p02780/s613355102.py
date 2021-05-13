import sys
import math
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":
    n,k = I2()
    p = Intl()
    s = 0
    for i in range(k):
        s += (p[i] + 1)/2
    ans = s
    for i in range(k,n):
        s += (p[i] + 1)/2
        s -= (p[i-k] + 1)/2
        ans = max(ans,s)
    print(ans)