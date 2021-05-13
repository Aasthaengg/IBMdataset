n = int(input())
s = input()

cnt_e = [0] * (n + 1)
for i in range(n):
    if s[i] == 'E':
        cnt_e[i+1] = cnt_e[i] + 1
    else:
        cnt_e[i+1] = cnt_e[i]

cnt_w = [0] * (n + 1)
for i in range(n, 0, -1):
    if s[i-1] == 'W':
        cnt_w[i-1] = cnt_w[i] + 1
    else:
        cnt_w[i-1] = cnt_w[i]

res = 0
for i in range(n):
    res = max(res, cnt_e[i] + cnt_w[i+1])

print(n - res - 1)