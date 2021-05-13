while True:
    s = input()
    if int(s) == 0:
        break;
    ans = 0
    for i in s:
        ans += int(i)
    print(ans)