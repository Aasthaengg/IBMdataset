import sys
def input():
    return sys.stdin.readline()[:-1]
def main():
#    N = int(input())
    A, B = map(int,input().split())
#    S = input()
    if A >= 13:
        print(B)
    elif A >= 6:
        print(B//2)
    else:
        print(0)
if __name__ == '__main__':
    main()
