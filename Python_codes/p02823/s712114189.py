import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    N,A,B=map(int,input().split())
    if (A-B)%2==0:
        print(abs(A-B)//2)
    else:
        print(min(A-1+1+((B-1)-(A-1))//2,\
                N-B+1+(N-(A+N-B+1))//2))


resolve()