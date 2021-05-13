import sys

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N, K = mi()
    ans = 0
    for b in range(K+1, N+1):
        q = 0
        while K+b*q <= N:
            ans += min((q+1)*b, N+1)-(K+b*q)
            q += 1
    if K == 0:
        ans -= N
    print(ans)


if __name__ == '__main__':
    main()
