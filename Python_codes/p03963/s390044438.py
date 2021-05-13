def main():
    N, K = (int(i) for i in input().split())
    ans = K
    ans *= pow(K-1, N-1)
    print(ans)


if __name__ == '__main__':
    main()
