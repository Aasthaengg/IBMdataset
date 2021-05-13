import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():
        N,M,K=map(int,input().split())
        for k in range(N+1):
            for l in range(M+1):
                if K==k*M+l*N-k*l*2:
                    return 'Yes'
        return 'No'

    print(main())



resolve()