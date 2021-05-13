import sys
import math
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":
    n ,y = I2()
    for i in range(n+1):
        for j in range(n+1-i):
            k = n - i - j
            if y//1000 == 10*i + 5*j + k:
                print(i,j,k)
                exit()
    print(-1,-1,-1)