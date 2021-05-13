def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
#from math import gcd
from fractions import gcd
n,m = iim()
s = input()
t = input()
num = gcd(n,m)
lcm = n*m//num
print(lcm if s[::n//num] == t[::m//num] else -1)
