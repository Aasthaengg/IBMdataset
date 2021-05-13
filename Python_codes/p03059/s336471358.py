import sys
input = sys.stdin.readline
def main():
    A, B, T = map(int, input().split())
    BIS = int((T+0.5)//A * B)
    print(BIS)

if __name__ == '__main__':
    main()