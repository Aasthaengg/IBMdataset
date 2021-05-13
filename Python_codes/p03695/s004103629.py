import sys
import math
import itertools as it
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

def f(rate):
    global zero
    color = [400,800,1200,1600,2000,2400,2800,3200]
    for i in range(8):
        if rate < color[i]:
            return i
if __name__ == "__main__":
    cnt = [0,0,0,0,0,0,0,0]
    n = I()
    a = Intl()
    zero = 0
    ans = 0
    for i in a:
        if i < 3200:cnt[f(i)] = 1
        else:zero += 1
    #print(cnt)
    print(max(1,sum(cnt)),sum(cnt)+zero)