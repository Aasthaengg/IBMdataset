A, B = map(int, input().split())
cnt = 0
for i in range(A, B+1):
    f = True
    str_i = str(i)
    lim = int(len(str_i) / 2)
    for j in range(lim):
        if str_i[j] != str_i[-j-1]:
            f = False
    if f:
        cnt += 1
print(cnt)