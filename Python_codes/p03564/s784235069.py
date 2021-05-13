import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    K=ii()

    ans = INF
    for a in range(N+1):
        b = N-a
        res = 1
        for i in range(a):
            res *= 2

        for j in range(b):
            res += K

        ans = min(ans,res)

    
    print(ans)


    


if __name__ == "__main__":
    main()