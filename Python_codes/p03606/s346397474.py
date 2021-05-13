def resolve():
    n = int(input())
    lr_list = list()
    for i in range(n):
        a = list(map(int, input().split()))
        lr_list.append(a)

    ans = 0
    for i in range(n):
        groupe = lr_list[i][1] - lr_list[i][0] + 1
        ans += groupe
    print(ans)
resolve()