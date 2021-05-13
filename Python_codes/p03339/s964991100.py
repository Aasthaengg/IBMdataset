n = int(input())
s = input()

count_e = [0] * n
count_w = [0] * n
for i in range(n):
    if i == 0:
        if s[i] == 'E':
            count_e[i] = 1
        else:
            count_w[i] = 1
        continue
    if s[i] == 'E':
        count_e[i] = count_e[i-1] + 1
        count_w[i] = count_w[i-1]
    else:
        count_e[i] = count_e[i-1]
        count_w[i] = count_w[i-1] + 1

ans = 10 ** 9
for i in range(n):
    if s[i] == 'E':
        e = count_e[-1] - count_e[i]
        w = count_w[i]
    else:
        e = count_e[-1] - count_e[i]
        w = count_w[i] - 1
    ans = min(ans,e+w)
print(ans)