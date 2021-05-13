def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N = ii()
    K = ii()
    ans = 1
    for i in range(N):
        ans = min(ans+K, 2*ans)
    print(ans)

if __name__ == '__main__':
    main()