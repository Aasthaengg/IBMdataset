def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N = ii()
    S = input()
    m = max(len(set(S[:i]) & set(S[i:])) for i in range(N))
    print(m)

if __name__ == '__main__':
    main()