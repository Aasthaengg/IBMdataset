N = int(input())
L = []
res = []

for i in range(N):
    S = input()
    L.append(S)

L.sort()

max_cnt = 0
cnt = 0

L.append(0)

for i in range(len(L) - 1):
    if L[i] == L[i+1]:
        cnt += 1
    else:
        if cnt > max_cnt:
            max_cnt = cnt
            res = []
            res.append(L[i])
        elif cnt == max_cnt:
            res.append(L[i])
        cnt = 0

for i in res:
    print(i)