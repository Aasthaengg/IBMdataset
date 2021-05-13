n = int(input())
now_ls = list(map(int, input().split()))
target_ls = list(map(int, input().split()))
if sum(now_ls) < sum(target_ls):
    print(-1)
else:
    ans = 0
    lack = 0
    surplus_ls = []
    for i in range(n):
        if now_ls[i] < target_ls[i]:
            ans += 1
            lack += target_ls[i] - now_ls[i]
        else:
            surplus_ls.append(now_ls[i] - target_ls[i])
    surplus_ls.sort()
    while lack > 0:
        ans += 1
        nex = surplus_ls.pop()
        lack -= nex
    print(ans)


