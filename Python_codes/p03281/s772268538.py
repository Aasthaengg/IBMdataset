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
    def f(x):
        cnt = 0
        i = 1
        while i <= x:
            if x % i == 0:
                cnt += 1
            i += 1
        return cnt
    cnt = 0
    n = I()
    for i in range(1,n+1,2):
        if f(i) == 8:cnt += 1
    print(cnt)