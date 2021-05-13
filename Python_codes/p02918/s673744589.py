n, k = map(int, input().split())
s = list(input())

import copy

# left to right, change L into R
cnt = 0
tmp_s = copy.deepcopy(s)
flag = 1
for i, j in enumerate(s):
    if j == 'L':
        tmp_s[i] = 'R'
        if flag:
            cnt += 1
            flag = 0
    else:
        tmp_s[i] = 'R'
        flag = 1

    if cnt >= k and flag:
        break

cnt = 0
for i in range(n):
    if tmp_s[i] == 'R' and i != n-1 and tmp_s[i+1] == 'R':
        cnt += 1
    elif tmp_s[i] == 'L' and i != 0 and tmp_s[i-1] == 'L':
        cnt += 1

ans = cnt
# right to left, change L into R
cnt = 0
tmp_s = copy.deepcopy(s)
flag = 1
for i in range(n-1, -1, -1):
    j = s[i]
    if j == 'L':
        tmp_s[i] = 'R'
        if flag:
            cnt += 1
            flag = 0
    else:
        tmp_s[i] = 'R'
        flag = 1

    if cnt >= k and flag:
        break

cnt = 0
for i in range(n):
    if tmp_s[i] == 'R' and i != n-1 and tmp_s[i+1] == 'R':
        cnt += 1
    elif tmp_s[i] == 'L' and i != 0 and tmp_s[i-1] == 'L':
        cnt += 1

ans = max(ans, cnt)

# left to right, change R into L
cnt = 0
tmp_s = copy.deepcopy(s)
flag = 1
for i, j in enumerate(s):
    if j == 'R':
        tmp_s[i] = 'L'
        if flag:
            cnt += 1
            flag = 0
    else:
        tmp_s[i] = 'L'
        flag = 1

    if cnt >= k and flag:
        break

cnt = 0
for i in range(n):
    if tmp_s[i] == 'R' and i != n-1 and tmp_s[i+1] == 'R':
        cnt += 1
    elif tmp_s[i] == 'L' and i != 0 and tmp_s[i-1] == 'L':
        cnt += 1

ans = max(ans, cnt)

# right to left, change L into R
cnt = 0
tmp_s = copy.deepcopy(s)
flag = 1
for i in range(n-1, -1, -1):
    j = s[i]
    if j == 'R':
        tmp_s[i] = 'L'
        if flag:
            cnt += 1
            flag = 0
    else:
        tmp_s[i] = 'L'
        flag = 1

    if cnt >= k and flag:
        break

cnt = 0
for i in range(n):
    if tmp_s[i] == 'R' and i != n-1 and tmp_s[i+1] == 'R':
        cnt += 1
    elif tmp_s[i] == 'L' and i != 0 and tmp_s[i-1] == 'L':
        cnt += 1

ans = max(ans, cnt)

print(ans)