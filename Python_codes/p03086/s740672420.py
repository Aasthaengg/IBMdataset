s = input()

acgt = 'ACGT'
res = cnt = 0
for i in s:
    if i in acgt:
        cnt += 1
    else:
        res = max(cnt, res)
        cnt = 0
res = max(cnt, res)
print(res)
