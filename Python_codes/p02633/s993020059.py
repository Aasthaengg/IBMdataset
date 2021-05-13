#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys
input = sys.stdin.readline
inp = lambda :int(input())
ip = lambda :[int(w) for w in input().split()]

from fractions import gcd
x = inp()
ans = 360//gcd(360,x)
print(ans)

