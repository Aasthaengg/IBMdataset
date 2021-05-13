import sys
import math
import itertools as it
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

def f(a,b):
    if a == b:
        return True
    return False
if __name__ == "__main__":
    s = L()
    for i in range(1,len(s)-1):
        a = s[:len(s)-i]
        n = len(a)
        #print(a[:n//2],a[n//2:])
        if (f(a[:n//2],a[n//2:])):
            print(n)
            break