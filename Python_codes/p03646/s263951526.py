import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main(): 
    K = II()
    N = 50

    div, mod = divmod(K, N)

    li = list(range(div, div+N))

    for _ in range(mod):
        li.sort()
        li = [li[0]+N] + [i-1 for i in li[1:]]

    print(N)
    print(' '.join(map(str, li)))

main()