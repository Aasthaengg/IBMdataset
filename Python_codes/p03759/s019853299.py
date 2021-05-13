import sys
MAX_INT = int(10e12)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

a,b,c = IL()
if b*2 == a + c:
  print("YES")
else:
  print("NO")