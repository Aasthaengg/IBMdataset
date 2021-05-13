import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    A,B=map(int,input().split())
    print('Possible' if A%3==0 or B%3==0 or (A+B)%3==0 else 'Impossible')

resolve()