import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    A,B,C=mi()
    X = set()
    y = 0
    for x in [A,B,C]:
        if x in X: y = x
        X.add(x)

    for x in [A,B,C]:
        if x != y:
            print(x)
            exit()





if __name__ == "__main__":
    main()