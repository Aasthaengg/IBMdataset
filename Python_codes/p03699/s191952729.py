def main():
    N = int(input())
    s = [int(input()) for _ in range(N)]
    s.sort()

    ans = sum(s)
    if ans % 10 != 0:
        print(ans)
        exit()
    else:
        for ss in s:
            tmp = ans - ss
            if tmp % 10 != 0:
                print(tmp)
                exit()

    print(0)


if __name__ == "__main__":
    main()
