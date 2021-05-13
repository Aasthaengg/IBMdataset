import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    A,B=mi()
    if B % A == 0:
        print(A+B)
    else:
        print(B-A)




if __name__ == "__main__":
    main()