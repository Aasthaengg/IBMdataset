import sys
def input():
    return sys.stdin.readline()[:-1]
def main():
#    N = int(input())
    S, W = map(int,input().split())
#    S = input()
    print("safe" if S > W else "unsafe")
if __name__ == '__main__':
    main()
