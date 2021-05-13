S = input()
news = S.replace('BC', 'D')

ans, cnt = 0, 0
for s in news:
    if s == 'A':
        cnt += 1
    elif s == 'D':
        ans += cnt
    else:
        cnt = 0

print(ans)