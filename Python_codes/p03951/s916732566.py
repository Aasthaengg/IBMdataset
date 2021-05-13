import sys
import math
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":
    n = I()
    s = S()
    t = S()
    cnt = 0
    for i in range(n):
        #print(s[i:n],t[:n-i])
        now = 0
        for j in range(n-i):
            if s[i:n][j] == t[:n-i][j]:now += 1
        cnt = max(cnt,now)
    print(2 * n - cnt)