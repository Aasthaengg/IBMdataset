import sys
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

a,b=mp()
if (b-a)%2==0:
    print((a+b)//2)
else:
    print("IMPOSSIBLE")