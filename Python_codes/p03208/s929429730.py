def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N, K = mi()
    h = [ii() for _ in range(N)]
    h.sort()
    print(min(h[i+K-1]-h[i] for i in range(N-K+1)))

if __name__ == '__main__':
    main()