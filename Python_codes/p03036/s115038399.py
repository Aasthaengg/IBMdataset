import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

r,D,x = LI()
temp = x
for _ in range(10):
   temp = r * temp - D
   print(temp)