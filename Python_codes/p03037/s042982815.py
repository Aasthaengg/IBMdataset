import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N,M = LI()
left = 0
right = 10000000

for _ in range(M):
    l,r = LI()
    left = max(left,l)
    right = min(right,r)

count = 0
for i in range(1,N+1):
    if left <= i <= right:
        count += 1
print(count)