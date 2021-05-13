def main():
    N, K = map(int, input().split())
    if N % K == 0: return 0
    else: return 1


if __name__ == '__main__':
    print(main())