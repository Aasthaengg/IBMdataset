import sys
import math
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":
    a, b, c, d = I2()
    #bまでのc,dの倍数 - a-1以下のc,dの倍数 重複分を加算
    cnt = b - a + 1
    cnt -= b//c
    cnt += (a-1)//c
    cnt -= b//d
    cnt += (a-1)//d
    cnt += b//(c*d//math.gcd(c,d))
    cnt -= (a-1)//(c*d//math.gcd(c,d))
    print(cnt)
