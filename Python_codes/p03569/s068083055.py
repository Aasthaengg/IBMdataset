import sys

S = sys.stdin.readline().rstrip()
not_x = []

for i, s in enumerate(S):
    if s != "x":
        not_x.append(s)

not_x_nums = len(not_x)
mid = not_x_nums // 2

if not_x_nums % 2 == 1:
    left = not_x[:mid]
    right = not_x[mid + 1:][::-1]
else:
    left = not_x[:mid]
    right = not_x[mid:][::-1]

if left == right:
    ans = 0
    left = []
    right = []
    tmp = 0
    cnt = 0
    if not_x_nums % 2 == 1:
        mid += 1
    for s in S:
        if s != "x":
            left.append(tmp)
            tmp = 0
            cnt += 1
        else:
            tmp += 1
        if cnt == mid:
            break
    tmp = 0
    cnt = 0
    for s in S[::-1]:
        if s != "x":
            right.append(tmp)
            tmp = 0
            cnt += 1
        else:
            tmp += 1
        if cnt == mid:
            break
    for l, r in zip(left, right):
        ans += abs(l - r)
    print(ans)
else:
    print(-1)