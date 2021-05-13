import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    ans = 0
    for i in range(1,N+1):
        if i % 3 != 0 and i % 5 != 0:
            ans += i
    
    print(ans)




if __name__ == "__main__":
    main()