def main():
    N = int(input())
    if N % 2 == 1:
        print(0)
    else:
        N //= 2
        ans = 0
        i = 0
        while True:
            i += 1
            v = 5 ** i
            if v > N:
                break
            else:
                ans += N // v
        print(ans)


if __name__ == '__main__':
    main()
