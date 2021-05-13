import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

mi = min(a,b,c,d,e)
t = (n + (mi - 1)) // mi
print(4 + t)
