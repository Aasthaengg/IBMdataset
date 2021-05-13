import string
s = input()
n = len(s)

min_cnt = float('inf')

for c in string.ascii_lowercase:
    if c not in s:
        continue
    cnt = 0
    s_ = s[:]
    while s_:
        m = len(s_) - 1
        is_same = True
        for d in s_:
            if d != c:
                is_same = False
                break
        if is_same:
            min_cnt = min(min_cnt, n - m-1)
        s_next = [''] * m
        for i in range(m):
            if s_[i] == c or s_[i + 1] == c:
                s_next[i] = c
            else:
                s_next[i] = s_[i]
        s_ = s_next

print(min_cnt)
