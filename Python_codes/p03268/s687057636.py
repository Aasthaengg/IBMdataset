import sys
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    
    ans = (N//K)**3
    if K%2==0:
        ans += (N//(K//2) - N//K)**3
    print(ans)
    


if __name__ == '__main__':
    main()