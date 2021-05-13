s = input()
t = input()
if s.count(t):
    print(0)
else:
    len_t = len(t)
    cnt = 0
    for i in range(len(s) - len_t + 1):
        c = 0
        for j in range(len_t):
            if s[i+j] == t[j]: c += 1
        cnt = max(cnt, c)
    print(len_t - cnt)