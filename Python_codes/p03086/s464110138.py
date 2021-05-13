S = input()
S += '*'
cnt = 0
ans = 0

for i in S:
    if i in ('A', 'C', 'G', 'T'):
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
print(ans)