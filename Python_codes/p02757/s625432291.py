from collections import defaultdict

N, P = map(int, input().split())
S = input()

if P in (2, 5):
    count = 0
    for i in range(N):
        if int(S[i]) % P == 0:
            count += i + 1
    print(count)
else:
    d = defaultdict(int)
    r = 0
    for i in range(N):
        r += int(S[N - 1 - i]) * pow(10, i % (P - 1), P)
        r %= P
        d[r] += 1

    count = d[0]
    for num in d.values():
        count += num * (num - 1) // 2
    print(count)