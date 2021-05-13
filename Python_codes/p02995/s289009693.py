import bisect,collections,copy,heapq,itertools,math,string
import sys
def li(): return map(int,sys.stdin.readline().rstrip().split())
def lf(): return map(float,sys.stdin.readline().rstrip().split())
def ls(): return sys.stdin.readline().rstrip().split()

a, b, c, d = li()
cn = b//c - (a-1)//c
dn = b//d - (a-1)//d
lcm = c*d//math.gcd(c,d)
cdn = b//lcm - (a-1)//lcm
print(b-a+1-cn-dn+cdn)