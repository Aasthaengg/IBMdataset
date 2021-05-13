N, W = map(int, input().split())

w = [[] for _ in range(4)]
w1, v1 = map(int, input().split())
w[0].append(v1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    w[a - w1].append(b)

for i in range(4):
    w[i].sort(reverse = True)
    for j in range(1, len(w[i])):
        w[i][j] += w[i][j - 1]

# print (w)
ans = 0
for a in range(len(w[0]) + 1):
    if a == 0:
        v_a = 0
    else:
        v_a = w[0][a - 1]
    for b in range(len(w[1]) + 1):
        if b == 0:
            v_b = 0
        else:
            v_b = w[1][b - 1]
        for c in range(len(w[2]) + 1):
            if c == 0:
                v_c = 0
            else:
                v_c = w[2][c - 1]
            cost = a * w1 + b * (w1 + 1) + c * (w1 + 2)
            if cost > W:
                pass
            else:
                lest = W - cost
                d = min(lest // (w1 + 3), len(w[3]))
                # print (d)
                if d == 0:
                    v_d = 0
                else:
                    v_d = w[3][d - 1]

                ans = max(ans, v_a + v_b + v_c + v_d)

print (ans)            
