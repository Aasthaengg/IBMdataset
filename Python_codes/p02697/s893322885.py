import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N,M = MI()

if N % 2 == 1:
    for i in range(M):
        print(i+1,N-i)
else:
    if N % 4 == 0:
        for i in range(min(M,N//4)):
            print(i+1,N-i)
        if M > N//4:
            for i in range(M-N//4):
                print(N//4+i+1,(3*N)//4-i-1)
    else:
        for i in range(min(M,N//4)):
            print(i+1,N-i)
        if M > N//4:
            for i in range(M-N//4):
                print(N//4+i+1,N-N//4-i-1)
