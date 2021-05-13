def resolve():
    N = int(input())
    a = list(map(int, input().split()))
    dic = dict()
    for i, an in enumerate(a):
        dic[i + 1] = an
    ans = 0
    # print('dic', dic)
    for d in dic.keys():
        if dic[dic[d]] == d:
            ans += 1
    ans = int(ans/2)
    print(ans)
    return
resolve()