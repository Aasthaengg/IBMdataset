import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    A=list(mi())

    r = 0
    asum = 0
    xsum = 0
    ans = 0
    for l in range(N):
        while r < N and asum+A[r] == xsum^A[r]:
            asum += A[r]
            xsum ^= A[r]
            r += 1

        # print(r)
        ans += r-l
        if l == r:
            r += 1
        else:
            asum -= A[l]
            xsum ^= A[l]
        
        
    print(ans)



    


if __name__ == "__main__":
    main()