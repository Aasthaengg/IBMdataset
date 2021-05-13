n, *a = map(int, open(0).read().split())
a.append('*')
cnt = 0
tmp_cnt = 0
tmp = '*'
for i in range(n+1):
    if a[i] == tmp:
        tmp_cnt += 1
    else:
        cnt += tmp_cnt//2
        tmp = a[i]
        tmp_cnt = 1
print(cnt)