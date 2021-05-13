import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    A,B=mi()
    if A <= 5:
        print(0)
    elif 6<=A<=12:
        print(B//2)
    else:
        print(B)




if __name__ == "__main__":
    main()