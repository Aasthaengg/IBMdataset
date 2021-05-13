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
    s = [S() for _ in range(h)]
    for i in range(1,h-1):
        for j in range(1,w-1):
            if(s[i][j] == "#" and s[i][j-1]!="#" and s[i][j+1]!="#" and s[i-1][j]!="#" and s[i+1][j] != "#"):
                print("No")
                exit()
    print("Yes")