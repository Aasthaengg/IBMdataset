import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N,X=mi()
    M = []
    for i in range(N):
        m = ii()
        M.append(m)

    M.sort()
    X -= sum(M)
    k = X//M[0]
    X -= k*M[0]

    print(N+k)
        



if __name__ == "__main__":
    main()