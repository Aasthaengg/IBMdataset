S = input().replace('BC', 'X')

cnt = 0
ans = 0
for s in S[::-1]:
    if s == 'X':
        cnt += 1
    elif s == 'A':
        ans += cnt
    else:
        cnt = 0

print(ans)