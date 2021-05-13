import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    r,D,x=mi()
    for i in range(10):
        x = x*r - D
        print(x)
        




if __name__ == "__main__":
    main()