import sys
from math import gcd
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N,M = MI()
A = LI()

x = sum(a % 2 == 0 for a in A)
if x != N:  # 奇数が含まれたら駄目
    print(0)
    exit()

r = 0
while A[0] % 2 == 0:
    r += 1
    A[0] //= 2
for i in range(1,N):
    if A[i] % (2**r) != 0 or (A[i]//(2**r)) % 2 == 0:  # 2で割り切れる回数が異なるものがあったら駄目
        print(0)
        exit()
    else:
        A[i] //= 2**r

lcm = A[0]
for i in range(1,N):
    lcm = (lcm*A[i])//gcd(lcm,A[i])

a = (lcm*2**r)//2

# a の奇数倍で、M 以下である整数の個数が答え

print(((M//a)+1)//2)
