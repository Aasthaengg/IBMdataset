import sys
def LI(): 
    return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,K = LI()

if N % K == 0:
    print(0)
else:
    print(1)