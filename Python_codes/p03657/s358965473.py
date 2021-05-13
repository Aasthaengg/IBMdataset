import sys
input = sys.stdin.readline
A,B = [int(i) for i in input().split()]
ma = A % 3
mb = B % 3
mp = (A+B) % 3
if ma == 0 or mb == 0 or mp == 0 :
    print("Possible")
else :
    print("Impossible")