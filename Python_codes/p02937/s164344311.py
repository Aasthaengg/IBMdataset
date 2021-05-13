from bisect import bisect_left

S = input()
T = input()
N = len(S)
NN = len(T)
S = [ord(S[i]) - 97 for i in range(N)]
T = [ord(T[i]) - 97 for i in range(NN)]

ind = [[] for _ in range(26)]
cnt = [0] * 26
for i in range(N):
    s = S[i]
    ind[s].append(i)
    cnt[s] += 1

part = 0
i = 0
j = -1
cond = 0
while i < NN:
    obj = T[i]
    if cnt[obj] == 0:
        cond = 1
        break

    tmp = bisect_left(ind[obj], j)
    if tmp == cnt[obj]:
        j = ind[obj][0]
        part += 1
        i += 1
        continue
    if ind[obj][tmp] == j:
        tmp += 1

    if tmp == cnt[obj]:
        j = ind[obj][0]
        part += 1
    else:
        j = ind[obj][tmp]

    i += 1


if cond:
    ans = -1
else:

    ans = N * part + (j + 1)

print(ans)