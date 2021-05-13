def resolve():
    S = input()
    ans, cnt = 0, 0
    for s in S:
        if s == 'A' or s == 'C'or s == 'G' or s == 'T':
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

resolve()
