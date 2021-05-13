def main():
    n, k = map(int, input().split())
    s = list(map(int, list(input())))

    # Cumulative Sum
    cs = [0]
    now = 1
    cnt = 0
    for i in s:
        if i == now:
            cnt += 1
        else:
            cs.append(cs[-1] + cnt)
            now = i
            cnt = 1
    cs.append(cs[-1] + cnt)
    if now == 0:
        cs.append(cs[-1])

    if len(cs) - 2*k - 1 < 1:
        print(n)
    else:
        ans = 0
        for i in range(0, len(cs)-2*k-1, 2):
            cnt = cs[i + 2*k + 1] - cs[i]
            if ans < cnt:
                ans = cnt
        print(ans)

main()