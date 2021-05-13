gene = {'A', 'T', 'G', 'C'}
s = input().strip()     #;print(s)

cnt = 0; ans = 0
for w in s:
    if w in gene:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
print(max(ans, cnt))