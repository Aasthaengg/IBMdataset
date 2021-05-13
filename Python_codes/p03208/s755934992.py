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
    n ,k = I2()
    h = [I() for _ in range(n)]
    h.sort()
    ans = float("inf")
    for i in range(n-k+1):
        a,b = h[i],h[i+k-1]
        #print(a,b)
        ans = min(ans,b-a)
    print(ans)