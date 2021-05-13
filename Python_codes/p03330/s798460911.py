import itertools

n, c = map(int, input().split())
d = []
for i in range(c):
    di = list(map(int, input().split()))
    d.append(di)
dic0 = {}
dic1 = {}
dic2 = {}
for i in range(1, n+1):
    ci = list(map(int, input().split()))
    for j in range(n):
        cj = ci[j]
        if (i+j+1)%3 == 0:
            if cj in dic0:
                dic0[cj] += 1
            else:
                dic0[cj] = 1
        elif (i+j+1)%3 == 1:
            if cj in dic1:
                dic1[cj] += 1
            else:
                dic1[cj] = 1
        else:
            if cj in dic2:
                dic2[cj] += 1
            else:
                dic2[cj] = 1

ans = 10**9
for c0, c1, c2 in itertools.permutations(list(range(1, c+1)), 3):
    temp = 0
    for key in dic0.keys():
        if key != c0:
            temp += d[key-1][c0-1] * dic0[key]
    for key in dic1.keys():
        if key != c1:
            temp += d[key-1][c1-1] * dic1[key]
    for key in dic2.keys():
        if key != c2:
            temp += d[key-1][c2-1] * dic2[key]
    ans = min(ans, temp)
print(ans)