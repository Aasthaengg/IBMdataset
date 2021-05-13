def main():
    n, d = map(int, input().split())
    # 2d + 1が1人の範囲
    # nを (2*d + 1)で割り切れたらそのまま、割り切れなかったら整数部分 + 1
    ans = n / (2*d + 1)
    if ans.is_integer():
        print(int(ans))
    else:
        print(int(ans) + 1)

if __name__ == '__main__':
    main()