def codef(S):
    # 条件に合う文字列か判別
    s_tmp = S.replace("x", "")
    for i, j in zip(s_tmp, s_tmp[::-1]):
        if i != j:
            return -1

    cnt = 0
    x_cnt = []
    for s in S:
        if s == "x":
            cnt += 1
        else:
            x_cnt.append(cnt)
            cnt = 0
    x_cnt.append(cnt)

    res = sum(abs(x-y) for x, y in zip(x_cnt, x_cnt[::-1])) // 2
    return res


if __name__ == "__main__":
    s = input()
    ans = codef(s)
    print(ans)
