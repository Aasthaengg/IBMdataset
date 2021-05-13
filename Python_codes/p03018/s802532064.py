S = input().replace('BC', 'D')
ans = 0
cnt = 0
for s in S:
    if s=='A':
        cnt += 1
    elif s=='D':
        ans += cnt
    else:
        cnt = 0
print(ans)