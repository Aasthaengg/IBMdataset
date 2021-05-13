def main():
    n = int(input())
    inlis = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        flg = 0
        a = inlis[i]
        while flg == 0:
            if a % 2 != 0:
                flg += 1
            else:
                ans += 1
                a /= 2
    print(ans)
        



if __name__ == "__main__":
    main()