import itertools
s = input()
n = len(s)
keep = []
num = 0
ans = [0] * len(s)
gr = itertools.groupby(s)
for key, group in gr:
    keep.append([key, len(list(group))])
ans_num = 0
for i in range(len(keep)):
    if keep[i][0] == "R":
        if ans_num + keep[i][1] == n:
            ans[n - 1] += keep[i][1]
        else:
            ans[ans_num + keep[i][1] - 1] += (keep[i][1] - 1) // 2 + 1
            ans[ans_num + keep[i][1]] += keep[i][1] // 2

    else:
        if ans_num == 0:
            ans[0] += keep[i][1]
        else:
            ans[ans_num] += (keep[i][1] - 1) // 2 + 1
            ans[ans_num - 1] += keep[i][1] // 2
    ans_num += keep[i][1]

re_ans = str(ans[0])
for i in range(1, n):
    re_ans = re_ans + " " + str(ans[i])


print(re_ans)
