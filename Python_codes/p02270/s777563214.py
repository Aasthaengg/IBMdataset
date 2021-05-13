n, k = [int(x) for x in input().split()]
w = [int(input()) for _ in range(n)]

P = 10 ** 4 * 10 ** 5

mi = 0
ma = P

while ma - mi > 1:
    ans = (ma + mi) // 2
    now = 0
    count = 1
    is_success = True
    for v in w:
        if now + v <= ans:
            now += v
        else:
            now = v
            count += 1
            if count > k or now > ans:
                mi = ans
                is_success = False
                break
    if is_success:
        ma = ans

print(ma)



