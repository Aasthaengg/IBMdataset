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
    h,w = I2()
    s = [L() for _ in range(h)]
    dx = [1,0,-1,0,1,-1,-1,1]
    dy = [0,1,0,-1,1,1,-1,-1]
    x,y = 0,0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":continue
            cnt = 0
            for k in range(8):
                x = j+dx[k]
                y = i+dy[k]
                if (y < 0 or h <= y):continue
                if (x < 0 or w <= x):continue
                if s[y][x] == "#":cnt += 1
            s[i][j] = cnt
    for i in s:
        for j in i:
            print(j,end="")
        print()