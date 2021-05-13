def main():
    _ = int(input())
    S, T = input().split()

    ans = ''
    for a, b in zip(S, T):
        ans += a + b
    print(ans)


if __name__ == '__main__':
    main()
