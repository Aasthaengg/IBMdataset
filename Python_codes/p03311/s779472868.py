import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N = I()
A = LI()
for i in range(N):
    A[i] -= i+1
A.sort()


def f(x):
    return sum(abs(A[i]-x) for i in range(N))


print(f((A[(N-1)//2]+A[N//2])//2))
# 中間値
