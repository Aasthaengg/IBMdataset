N = int(input())

ans = 0

kk = 1
for x in range(1, N + 1):
    ans_ = 0
    k = x
    for y in range(999):
        if x % 2 == 0:
            x /= 2
            ans_ += 1
        else:
            break
    if ans_ > ans:
        ans = ans_
        kk = k
print(kk)