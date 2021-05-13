import collections
N = int(input())
S = input()
_ = input()

c = collections.Counter(S)
instant = []
i = 0
while i < N:
    if c[S[i]] == 2:
        instant.append(2)
        i += 2
    else:
        instant.append(1)
        i += 1


if instant[0] == 2:
    ans = 6
else:
    ans = 3

for i in range(1, len(instant)):
    if instant[i-1] == 1:
        ans *= 2
    elif instant[i] == 2:
        ans *= 3

print(ans % (10 ** 9 + 7))