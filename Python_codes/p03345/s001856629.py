
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    A,B,C,K=map(int,input().split())
    if abs(B-A)>10**18:
        print('Unfair')
    else:
        if K%2==0:
            print(A-B)
        else:
            print(B-A)

resolve()