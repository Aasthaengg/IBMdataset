import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N,M,X = LI()
A =LI()
cost = 0
go_right = N-X
go_left = X
cost_right = 0
cost_left = 0
for i in range(X+1, N):
    if i in A:
        cost_right += 1

for j in range(1,X):
    if j in A:
        cost_left += 1

print(min(cost_left,cost_right))