def main():
    N = int(input())
    a = [int(input()) for _ in range(N)]
    i = 1
    cnt = 0
    flag = False

    for _ in range(N):
        cnt += 1
        i = a[i - 1]

        if i == 2:
            flag = True
            break

    if flag == True:
        print(cnt)
    else:
        print(-1)


if __name__ == "__main__":
    main()
