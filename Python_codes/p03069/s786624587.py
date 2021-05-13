import itertools
n = int(input())
s = [i for i in input()]
cnt_s, cnt_d = [0]*(n+1), [0]*(n+1)
for i in range(n):
    if s[i] == "#":
        cnt_s[i+1] = 1
    else:
        cnt_d[i+1] = 1
cnt_s, cnt_d = list(itertools.accumulate(cnt_s)), list(itertools.accumulate(cnt_d))
ans = 10**6
cnt_d_l = cnt_d[-1]
for i in range(n+1):
    ans = min(ans, cnt_s[i] - cnt_s[0] + (cnt_d_l - cnt_d[i]))
print(ans)