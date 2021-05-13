import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    A,B,N=mi()

    x = min(B-1,N)
    f = (A*x)//B - A*(x//B)
    
    print(f)

if __name__ == "__main__":
    main()