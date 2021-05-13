import sys
input = sys.stdin.readline
def main():
    A, P = map(int, input().split())
    S = A*3 + P
    print(S//2)

if __name__ == '__main__':
    main()