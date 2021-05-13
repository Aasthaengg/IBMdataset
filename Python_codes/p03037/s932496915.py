import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N,M=mi()

    L,R=-INF,INF
    for i in range(M):
        l,r = mi()
        if L < l:
            L = l
        if r < R:
            R = r
        
        if R < L:
            print(0)
            exit()
    
    print(R-L+1)



        





if __name__ == "__main__":
    main()