s = input() + "R"

rcnt = 0
lcnt = 0
tmp = "R"
ans = []

for c in s:
    if tmp == "R" and c == "R":
        rcnt += 1
    elif tmp == "R" and c == "L":
        tmp = "L"
        lcnt = 1

    elif tmp == "L" and c == "L":
        lcnt += 1

    elif tmp == "L" and c == "R":
        cnt = lcnt + rcnt
        for _ in range(rcnt - 1):
            ans.append(0)
        if (lcnt + rcnt) % 2 == 0:
            ans.append(cnt // 2)
            ans.append(cnt // 2)
        else:
            if rcnt % 2 == 0:
                ans.append(cnt // 2)
                ans.append(cnt // 2 + 1)
            else:
                ans.append(cnt // 2 + 1)
                ans.append(cnt // 2)
        for _ in range(lcnt - 1):
            ans.append(0)
        lcnt = 0
        rcnt = 1
        tmp = "R"
print(*ans)
