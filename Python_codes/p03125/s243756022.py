import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
def intinput():return map(int,input().split())

a,b=intinput()
print(a+b if b%a==0 else b-a)