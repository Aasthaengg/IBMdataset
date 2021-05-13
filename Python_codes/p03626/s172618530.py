def main():
    n = int(input())
    ls1 = list(input())
    ls2 = list(input())

    if ls1[0]==ls2[0]:
        ans = 3
        i =1
        flg = "b"
    else:
        ans = 6
        flg = "a"
        i =2

    while 1:

        if i >= n:
            break

        if ls1[i]==ls2[i]:
            if flg == "a":
                flg = "b"
            else:
                ans = (ans*2)%(10**9+7)

            i += 1

        else:
            if flg == "a":
                ans = (ans*3)%(10**9+7)
            else:
                ans = (ans*2)%(10**9+7)
                flg = "a"

            i += 2
        if i >= n:
            break

    print(ans)

if __name__ == "__main__":
    main()