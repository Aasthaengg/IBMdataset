n = int(input())
p = []
for i in range(n):
    num = int(input())
    num -= 1
    p.append(num)

cnt = [0] * n

for i in range(n):
    if p[i] == 0:
        cnt[0] = 1
    else:
        cnt[p[i]] = cnt[p[i] - 1] + 1

max_p = max(cnt)

print(n - max_p)