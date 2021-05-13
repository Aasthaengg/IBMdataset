import sys

input = sys.stdin.readline

def main():
    ans = 1
    N = int(input())
    for i in range(1,N+1):
        ans = ans*i%(10**9+7)
    print(ans)

if __name__ == '__main__':
    main()