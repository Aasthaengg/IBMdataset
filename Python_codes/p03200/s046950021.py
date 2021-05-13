def resolve():
    s = str(input())
    ans = 0
    ind = []
    for i, char in enumerate(s):
        if char == 'W':
            ind.append(i)
    lst = 0
    # print(ind)
    for i in ind:
        ans += (i - lst)
        lst += 1

    # idx = s.index('W')
    print(ans)
    return


resolve()