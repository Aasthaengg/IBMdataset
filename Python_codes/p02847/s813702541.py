import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    S = input()
    X = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

    for i in range(len(X)):
        if S == X[i]:
            print(7-i)






if __name__ == "__main__":
    main()