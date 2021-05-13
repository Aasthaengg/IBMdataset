import sys
def input():
    return sys.stdin.readline()[:-1]
def main():
    N = int(input())
#    A, B, C = map(int,input().split())
#    S = input()
    if N < 1200:
        print("ABC")
    elif N < 2800:
        print("ARC")
    else:
        print("AGC")
if __name__ == '__main__':
    main()
