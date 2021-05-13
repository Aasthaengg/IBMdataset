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
    a = Intl()
    cnt = 0
    def dfs(l):#区間i,jについて最小水やり回数を求める
        global cnt
        if l == [] or l == [0]:return
        elif 0 in l:#0の前と後ろで分割して探索
            i = l.index(0)
            dfs(l[:i])
            dfs(l[i+1:])
        else:
            l = [k-1 for k in l]
            cnt += 1
            dfs(l)
    dfs(a)
    print(cnt)