import math


S = input()
ls = len(S)
ans = [0] * ls
i = 0
while i < ls:
    r_count = 0
    l_count = 0
    j = i
    while j < ls and S[j] == 'R':
        r_count += 1
        j += 1

    k = j
    while k < ls and S[k] == 'L':
        l_count += 1
        k += 1
    ans[j - 1] = math.ceil(r_count / 2) + l_count // 2
    ans[j] = r_count // 2 + math.ceil(l_count / 2)
    i = k

print(' '.join(map(str, ans)))
