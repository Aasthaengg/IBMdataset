import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def I(): return int(sys.stdin.readline().rstrip())
N = I()
a = LI()
print(sum(a)-len(a))
