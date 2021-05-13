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
    a = list(set(a))
    b = list(set(b))
    cnt = 0
    for i in a:
        for j in b:
            if i == j:cnt += 1
    return cnt

if __name__ == "__main__":
    n = I()
    s = L()
    ans = 0
    for i in range(n):
        #print(s[:n-i],s[n-i:])
        ans = max(ans,f(s[:n-i],s[n-i:]))
    print(ans)