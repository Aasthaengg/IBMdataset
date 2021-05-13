import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
A = LI()
for i in range(N):
    A[i] = (A[i],i)
A.sort()

print(*[A[i][1]+1 for i in range(N)])
