def main():
    N = int(input())
    K = int(input())
    X = map(int, input().split())
    ans = 0
    for x in X:
        ans += min([x, K-x]) * 2
    print(ans)


if __name__ == '__main__':
    main()
