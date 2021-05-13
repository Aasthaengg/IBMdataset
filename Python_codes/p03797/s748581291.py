import sys;input = lambda : sys.stdin.readline()
n,m = map(int,input().split())
if m-2*n>=0:
    print(n+(m-2*n)//4)
else:
    print(m//2)
