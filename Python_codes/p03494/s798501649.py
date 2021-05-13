def main():
    n = int(input())
    a = map(int, input().split())

    ans = 0
    is_even = True

    while is_even:
        list_tmp = []
        for an in a:
            if an % 2 == 0:
                list_tmp.append(an / 2)
            else:
                is_even = False
                break
        if is_even:
            a = list_tmp
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
