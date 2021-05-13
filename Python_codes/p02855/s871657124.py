H, W, K = map(int, input().split())
L = []
for _ in range(H):
    s = input()
    row = []
    for j in range(len(s)):
        row.append(s[j])

    L.append(row)
# print(L)

ans = [[0] * W for _ in range(H)]
# ans[0][1] = 1
# print(ans[0][1])

color = 1
count = 0
for i in range(H):
    if '#' not in L[i]:
        for j in range(W):
            ans[i][j] = -1
        continue
    else:
        idx = 0
        while idx < W:
            count += 1
            # print(ans[i][idx])
            if L[i][idx] == '.':
                # print(ans[i][idx])
                ans[i][idx] = color

                # print(ans, i, idx)
                idx += 1
            else:
                # print(ans[i][idx])
                ans[i][idx] = color
                # print(ans, i, idx)
                if ('#' in L[i][idx + 1:]):
                    color += 1
                idx += 1
    color += 1

new_ans = []
count = 0
for v in ans:
    if -1 in v:
        count += 1
        continue

    if count != 0 and -1 not in v:
        new_ans.append(v)
        while count > 0:
            new_ans.append(v)
            count -= 1

    elif count == 0 and -1 not in v:
        new_ans.append(v)


if count != 0:
    while count > 0:
        new_ans.append(new_ans[-1])
        count -= 1


for i in new_ans:
    print(*i)
