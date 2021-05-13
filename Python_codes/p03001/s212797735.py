import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    W,H,x,y = mi()

    ans = '{:.10f}'.format(W*H/2)
    ans2 = 1 if x==W/2 and y==H/2 else 0
    print(ans,ans2)
    




if __name__ == "__main__":
    main()