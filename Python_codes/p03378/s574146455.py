import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N,M,X = MI()
A = LI()
a = sum(A[i] < X for i in range(M))
print(min(a,M-a))
