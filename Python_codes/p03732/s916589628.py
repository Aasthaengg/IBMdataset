from itertools import accumulate
n, W = [int(item) for item in input().split()]
wv = [[] for _ in range(4)]
for i in range(n):
    w, v = [int(item) for item in input().split()]
    if i == 0:
        w1 = w
    wv[w-w1].append(v)
for i in range(4):
    wv[i] = sorted(wv[i], reverse=True)
    wv[i] = [0] + list(accumulate(wv[i]))

ans = 0
for i in range(len(wv[0])):
    for j in range(len(wv[1])):
        for k in range(len(wv[2])):
            for l in range(len(wv[3])):
                if j*1 + k*2 + l*3 <= W - w1*(i+j+k+l):
                    ans = max(ans, wv[0][i] + wv[1][j] + wv[2][k] + wv[3][l])
print(ans)