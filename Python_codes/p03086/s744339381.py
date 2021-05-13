import sys
import math
import numpy as np
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":
    def f(s):
        if s == "":return 0
        t = s.replace("A","").replace("T","").replace("G","").replace("C","")
        if t == "":return len(s)
        else:return 0
    s = S()
    n = len(s)
    ans = 0
    cnt = 0
    for i in range(n):
        for j in range(i,n):
            t = s[i:j+1]
            ans = max(f(t),ans)
    print(ans)