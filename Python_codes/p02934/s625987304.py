import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
A = LI()

a = 0
for i in range(N):
    a += 1/A[i]

print(1/a)