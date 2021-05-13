import sys

def input(): return sys.stdin.readline().rstrip("\r\n")
def List(): return list(map(int, input().split()))
def Num(): return int(input())


x, k, d = List()
x = abs(x)
if d * k > x:
    distance = x % d
    do = k - (x // d)
    if do & 1:
        print(d - distance)
    else:
        print(distance)
else:
    print(x - k * d)
