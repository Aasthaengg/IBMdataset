def solve(STR):
    CNT, tmp = 0, s
    while len(set(tmp)) > 1:
        CNT += 1
        bfo, tmp = tmp, []
        for i in range(len(bfo) - 1):
            tmp.append(bfo[i])
            if STR in {bfo[i], bfo[i + 1]}:
                tmp[-1] = STR
    return CNT


s = input()

ans = 100
for lttr in set(s):
    cnt = solve(lttr)
    ans = min(ans, cnt)
print(ans)
