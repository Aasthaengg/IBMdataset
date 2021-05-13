import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

def main():
    A,B=mi()
    print(max(A+B,A+A-1,B+B-1))

                





if __name__ == "__main__":
    main()