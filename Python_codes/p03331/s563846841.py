n = int(input())

digis_sum = 10 ** 2

def cal_digit(num):
    tmp = 0
    q = num
    while q:
        q, r = divmod(q, 10)
        tmp += r
        if q == 0:
            break
    return tmp

for x in range(1, int(n/2)+1):
    y = n - x
    t = cal_digit(x) + cal_digit(y)
    if t < digis_sum:
        digis_sum = t

print(digis_sum)