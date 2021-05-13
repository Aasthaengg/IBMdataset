n = int(input())
la = list(map(int, input().split()))

d0 = {-1: 0}
for a in la[::2]:
    d0[a] = d0.get(a, 0) + 1
d1 = {-1: 0}
for a in la[1::2]:
    d1[a] = d1.get(a, 0) + 1

n0 = sorted([(v, k) for k, v in d0.items()], reverse=True)
n1 = sorted([(v, k) for k, v in d1.items()], reverse=True)


if n0[0][1] != n1[0][1]:
    answer = n - n0[0][0] - n1[0][0]
else:
    if n0[1][0] > n1[1][0]:
        answer = n - n0[1][0] - n1[0][0]
    else:
        answer = n - n0[0][0] - n1[1][0]


print(answer)
