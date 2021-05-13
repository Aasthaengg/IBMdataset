K = int(input())
A = tuple(map(int, input().split()))

l, r = 1, 10 ** 18
while r - l > 1:
    m = (l + r) // 2
    M = m
    for a in A:
        M = (M // a) * a

    if M <= 2:
        l = m
    else:
        r = m
ans_max = l

l, r = 1, 10 ** 18
while r - l > 1:
    m = (l + r) // 2
    M = m
    for a in A:
        M = (M // a) * a

    if M >= 2:
        r = m
    else:
        l = m
ans_min = r

if ans_min > ans_max:
    print(-1)
else:
    print(ans_min, ans_max)
