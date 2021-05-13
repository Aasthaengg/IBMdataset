import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    S=str(input())
    w=int(input())
    ls=len(S)
    L=[S[i*w] for i in range(-(-ls//w))]
    print(''.join(L))


    
resolve()