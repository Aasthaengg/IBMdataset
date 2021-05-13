import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    N=int(input())
    A=[int(input()) for i in range(N)]

    if all(i%2==0 for i in A):
        print('second')
    else:
        print('first')




resolve()