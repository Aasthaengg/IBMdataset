import bisect

N, H = map(int, input().split())

Attack = []
Throw = []
for _ in range(N):
    a, b = map(int, input().split())
    Attack.append(a)
    Throw.append(b)
attack = max(Attack)
Throw.sort()

Throw_num = bisect.bisect_left(Throw, attack)
Throw_sum = sum(Throw[Throw_num:])

if Throw_sum <= H:
    print((H - Throw_sum - 1) // attack + 1 + N - Throw_num)
else:
    Throw.sort(reverse=True)
    for i in range(N):
        H -= Throw[i]
        if H <= 0:
            print(i + 1)
            exit()

