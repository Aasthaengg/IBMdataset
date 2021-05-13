while True:
    x = input()
    if x == "0":
        break
    ans = 0
    for i in x:
        int_i = int(i)
        ans += int_i
    print(ans)

