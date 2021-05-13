ABCD = input()
for p in range(1 << 3):
    v = int(ABCD[0])
    ans = ABCD[0]
    for i in range(3):
        if p & (1 << i):
            v -= int(ABCD[i + 1])
            ans += '-' + ABCD[i + 1]
        else:
            v += int(ABCD[i + 1])
            ans += '+' + ABCD[i + 1]
    if v == 7:
        print(ans + '=7')
        exit()
