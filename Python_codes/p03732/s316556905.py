n,w = map(int,input().split())
wv = [list(map(int,input().split())) for _ in range(n)]

max1 = w // wv[0][0]
min1 = w // (wv[0][0] + 3)
seq = list(range(n))
ans = 0

w_min = wv[0][0]
w_list = [[] for _ in range(4)]

for wa,va in wv:
    w_list[wa-w_min].append(va)

for i in range(4):
    w_list[i].sort(reverse = True)

for i in range(4):
    for j in range(len(w_list[i])-1):
        w_list[i][j+1] += w_list[i][j]

for i in range(min1, max1+1):
    for w1 in range(i+1):
        for w2 in range(i-w1+1):
            for w3 in range(i-w1-w2+1):
                w4 = i - w1 - w2 - w3
                if w1 * w_min + w2 * (w_min+1) + w3 * (w_min+2) + w4 * (w_min+3) <= w:
                    if len(w_list[0]) >= w1 and len(w_list[1]) >= w2 and len(w_list[2]) >= w3 and len(w_list[3]) >= w4:
                        tmp = 0
                        if w1 >= 1:
                            tmp += w_list[0][w1-1]
                        if w2 >= 1:
                            tmp += w_list[1][w2-1]
                        if w3 >= 1:
                            tmp += w_list[2][w3-1]
                        if w4 >= 1:
                            tmp += w_list[3][w4-1]
                        ans = max(ans, tmp)

print(ans)
