import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N,P = MI()
A = LI()

x = sum(A[i] % 2 == 0 for i in range(N))  # Aiの中で、偶数であるものの個数
y = N-x  # Aiの中で、奇数であるものの個数

if y == 0:
    print(0 if P == 1 else 2**x)
else:
    print(2**(x+y-1))
