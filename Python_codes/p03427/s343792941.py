def resolve():
    N = int(input())
    N += 1

    ans = 0
    for i, n in enumerate(range(len(str(N)))):
        if i == 0:
            continue
        ans += int(9)
    ans += int(str(N)[0])-1
    print(ans)
    return


resolve()