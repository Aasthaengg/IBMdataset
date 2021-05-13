import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N = I()
A = LI()
for i in range(N):
    A[i] -= i+1
A.sort()

x = (A[N//2]+A[(N-1)//2])//2
print(sum(abs(A[i]-x) for i in range(N)))
