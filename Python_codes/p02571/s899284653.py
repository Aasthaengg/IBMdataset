def main():
    a = [input() for i in range(2)]
    S = a[0]
    T = a[1]
    count = 1001
    # 網羅的に一致しない文字数をカウント
    for i in range(len(S) - len(T) + 1):
        count_temp = 0
        for j in range(len(T)):
            if S[i + j] != T[j]:
                count_temp += 1
        count = min(count, count_temp)
        if count == 0:
            break
    print(count)


if __name__ == '__main__':
    main()