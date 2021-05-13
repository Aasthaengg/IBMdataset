def resolve():
    S = input()
    cnt = 0
    pre = ""
    tmp = ""
    for s in S:
        tmp += s
        if tmp != pre:
            pre = tmp
            tmp = ""
            cnt += 1
    print(cnt)


resolve()
