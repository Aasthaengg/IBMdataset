from collections import Counter
n = int(input())
ns = list(map(int, input().split()))
rslt = 0
a = 10 ** 9 + 7
cnt = Counter(ns)
if n % 2 == 0:
    for i in range(1, n, 2):
        if cnt[i] != 2:
            print(0)
            exit()
    rslt = pow(2, n // 2, a)
else:
    for i in range(2, n, 2):
        if cnt[i] != 2:
            print(0)
            exit()
    if cnt[0] == 1:
        rslt = pow(2, n // 2, a)
print(rslt)