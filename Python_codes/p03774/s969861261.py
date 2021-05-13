N, M = map(int, input().split())
a, b, ans = [], [], []
max0 = 10**10

for i in range(N):
    a += [list(map(int, input().split()))]

for i in range(M):
    b += [list(map(int, input().split()))]

for i in a:
    for j, k in enumerate(b):
        val = abs(i[0]-k[0])+abs(i[1]-k[1])
        if val < max0:
            pre = j
            max0 = val
    ans.append(pre+1)
    max0 = 10**10
[print(x) for x in ans]

