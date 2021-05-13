def main():
    s = input()
    K = int(input())
    lst = sorted(set(s))
    ans = ""
    cnt = 0

    def dfs(sub):
        nonlocal cnt, ans
        if cnt < K:
            ans = sub
            cnt += 1
            for li in lst:
                if sub + li in s:
                    dfs(sub + li)

    for li in lst:
        dfs(li)
    print(ans)
    return


main()
