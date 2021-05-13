def main():
    N = int(input())
    V = map(int, input().split())
    C = map(int, input().split())
    ans = 0
    for v, c in zip(V, C):
        if v - c > 0:
            ans += v - c
    print(ans)


if __name__ == '__main__':
    main()
