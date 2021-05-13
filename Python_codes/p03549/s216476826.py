import sys
input = sys.stdin.readline
def main():
    N, M = map(int, input().split())
    T = 100 *(N-M)
    ans = 2**M * (1900*M + (N-M)*100)
    print(ans)

if __name__ == '__main__':
    main()