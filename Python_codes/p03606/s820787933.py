import math

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N = ii()
    ans = 0
    for i in range(N):
        l, r = mi()
        ans += r-l+1
    print(ans)

if __name__ == '__main__':
    main()