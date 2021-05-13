import sys
sys.setrecursionlimit(100000)

def intinput(): return map(int,sys.stdin.readline().split())

t,x=intinput()
print(t/x)