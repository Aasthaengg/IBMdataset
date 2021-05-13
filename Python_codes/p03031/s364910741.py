n, m = map(int, input().split())
s = [list(map(int, input().split()))[1:] for _ in range(m)]
p = list(map(int, input().split()))
ans = 0

for i in range(2**n):
    status = ['+']*n
    for j in range(n):
        if ((i>>j)&1):
            status[j] = '-'
    num = 0
    for m, k in enumerate(s):
        count = 0
        for l in k:
            if status[l-1] == '+':
                count += 1
        if count%2 != p[m]:
            break
        else:
            num += 1
    if num == m+1:
        ans += 1
print(ans)
