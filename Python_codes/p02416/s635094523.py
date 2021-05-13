while True:
    inp = input()
    if inp == '0':
        break
    ans = 0
    for i in inp:
        ans += int(i)
    print(ans)

