N = int(input())
S = input()

cnt = 0
for i in range(1000):
    num = "{:03d}".format(i)
    fst = S.find(num[0])
    if fst == -1:
        continue
    sec = S.find(num[1], fst+1)
    if sec == -1:
        continue
    thr = S.find(num[2], sec+1)
    if thr == -1:
        continue

    cnt += 1

print(cnt)