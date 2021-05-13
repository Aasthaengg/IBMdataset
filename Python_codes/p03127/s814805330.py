from fractions import gcd

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N = ii()
    A = list(mi())
    ans = A[0]
    for i in range(N-1):
        ans = gcd(ans, A[i+1])
    print(ans)

if __name__ == '__main__':
    main()