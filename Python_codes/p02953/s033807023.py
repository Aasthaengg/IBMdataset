def main():
    N = int(input())
    H = list(map(int, input().split()))[::-1]
    for i in range(1, N):
        if H[i] - H[i-1] >= 2:
            print('No')
            exit()
        elif H[i] - H[i-1] == 1:
            H[i] -= 1
    print('Yes')


if __name__ == '__main__':
    main()
