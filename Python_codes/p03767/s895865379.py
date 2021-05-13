def main():
    N = int(input())  # 文字列または整数(一変数)
    a = list(map(int, input().split()))  # 整数のリスト

    answer = 0
    a.sort(reverse=True)

    for i in range(1, 2*N,2):
        answer += a[i]


    print(answer)

if __name__ == '__main__':
    main()
