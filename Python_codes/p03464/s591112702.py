K = int(input())
A = list(map(int, input().split()))


l = 0
r = 10 ** 20
while r - l > 1:
    m = (r + l) // 2
    N = m
    for a in A:
        N = (N//a)*a

    if N > 2:
        r = m
    else:
        l = m
upper = l


l = 0
r = 10 ** 20
while r - l > 1:
    m = (r + l) // 2
    N = m
    for a in A:
        N = (N//a)*a

    if N < 2:
        l = m
    else:
        r = m
lower = r

if lower > upper:
    print(-1)
else:
    print(lower, upper)
