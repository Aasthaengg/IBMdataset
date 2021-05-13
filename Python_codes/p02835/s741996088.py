import sys
def input():
    return sys.stdin.readline()[:-1]
def main():
#    N = int(input())
    A, B, C = map(int,input().split())
#    S = input()
    print("bust" if (A+B+C) >= 22 else "win")
if __name__ == '__main__':
    main()
