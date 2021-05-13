x = int(input())

divided_11 = x // 11
check_num = divided_11 * 11
ans = divided_11 * 2

if x % 11 == 0:
    print(ans)
else:
    while True:
        check_num += 6
        ans += 1
        if check_num >= x:
            print(ans)
            break
        check_num += 5
        ans += 1
        if check_num >= x:
            print(ans)
            break
