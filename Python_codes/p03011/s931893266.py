import sys
input = sys.stdin.readline
def main():
    P, Q, R = map(int, input().split())
    TIME = P+Q+R - max(P, max(Q, R))
    print(TIME)

if __name__ == '__main__':
    main()