import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    D=list(mi())

    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans += D[i]*D[j]

    print(ans)




if __name__ == "__main__":
    main()