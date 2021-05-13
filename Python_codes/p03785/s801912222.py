n, c, k = map(int, input().split())
T = list(int(input()) for _ in range(n))
T.sort()

lmt = 0
flg = True
tmp_c = c
bus_cnt = 0
for i in range(len(T)-1):
    if flg:
        lmt = T[i] + k
        flg = False
        bus_cnt += 1
    if tmp_c >= 0 or lmt >= T[i]:
        tmp_c -= 1
    if tmp_c <= 0 or lmt < T[i+1]:
        flg = True
        tmp_c = c
else:
    if tmp_c <= 0 or lmt < T[-1]:
        bus_cnt += 1

print(bus_cnt)