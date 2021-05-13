def resolve():
    a, b = map(int, input().split())
    count = 0
    for num in range(a, b+1):
        snum = str(num)
        if snum[0] != snum[4] or snum[1] != snum[3]:
            continue
        else:
            count += 1
    print(count)
resolve()