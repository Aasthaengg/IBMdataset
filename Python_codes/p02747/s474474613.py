import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    s=str(input())
    ls=len(s)
    if ls%2==1:
        print('No')
    else:
        if s=='hi'*(ls//2):
            print('Yes')
        else:
            print('No')


resolve()