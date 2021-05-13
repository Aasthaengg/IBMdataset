N, W = map(int, input().split())
V0, V1, V2, V3 = [], [], [], []
w0 = 0
for i in range(N):
    w, v = map(int, input().split())
    if i == 0:
        V0.append(v)
        w0 = w
    elif w0 == w:
        V0.append(v)
    elif w0 + 1 == w:
        V1.append(v)
    elif w0 + 2 == w:
        V2.append(v)
    else:
        V3.append(v)

V0 = sorted(V0, reverse=True)
V1 = sorted(V1, reverse=True)
V2 = sorted(V2, reverse=True)
V3 = sorted(V3, reverse=True)
vl0 = len(V0)
vl1 = len(V1)
vl2 = len(V2)
vl3 = len(V3)
V0_sum = [0] * (vl0 + 1)
V1_sum = [0] * (vl1 + 1)
V2_sum = [0] * (vl2 + 1)
V3_sum = [0] * (vl3 + 1)
for i in range(1, vl0 + 1):
    V0_sum[i] = V0_sum[i - 1] + V0[i - 1]
for i in range(1, vl1 + 1):
    V1_sum[i] = V1_sum[i - 1] + V1[i - 1]
for i in range(1, vl2 + 1):
    V2_sum[i] = V2_sum[i - 1] + V2[i - 1]
for i in range(1, vl3 + 1):
    V3_sum[i] = V3_sum[i - 1] + V3[i - 1]
w1, w2, w3 = w0 + 1, w0 + 2, w0 + 3
num = 0

for v0 in range(vl0 + 1):
    for v1 in range(vl1 + 1):
        for v2 in range(vl2 + 1):
            for v3 in range(vl3 + 1):
                w = v0 * w0 + v1 * w1 + v2 * w2 + v3 * w3
                if w <= W:
                    q = V0_sum[v0] + V1_sum[v1] + V2_sum[v2] + V3_sum[v3]
                    num = max(num, q)

print(num)
