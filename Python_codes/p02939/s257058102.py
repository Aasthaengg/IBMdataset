S = input()
cnt = 0
pre = ''
cr = ''
for ch in S:
    cr += ch
    if pre != cr:
        cnt += 1
        pre = cr
        cr = ''
print(cnt)