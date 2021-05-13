import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N,M=mi()

    X = [0]*(M+1)
    for i in range(N):
        Y = list(mi())
        for a in Y[1:]:
            X[a] += 1
    
    ans = 0
    for x in X:
        if x == N:
            ans += 1
    
    print(ans)
            
        



if __name__ == "__main__":
    main()