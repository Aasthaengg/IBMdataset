from collections import defaultdict

N = int(input())
X, Y = N-1, N
dic = defaultdict(int)
for p in range(2, int(N**0.5)+1):
    if X % p == 0:
        cnt = 0
        while X % p == 0:
            X //= p
            cnt += 1
        dic[p] = cnt
    if Y % p == 0:
        cnt = 0
        while Y % p == 0:
            Y //= p
            cnt += 1
        dic[p] = cnt
if X > 1:
    dic[X] = 1
if Y > 1:
    dic[Y] = 1
f = [1]
for p in dic.keys():
    f += [x*pow(p, c) for x in f for c in range(1, dic[p]+1)]
ans = 0
for x in f:
    if x == 1:
        continue
    y = N
    while y % x == 0:
        y //= x
    if y % x == 1:
        ans += 1
print(ans)