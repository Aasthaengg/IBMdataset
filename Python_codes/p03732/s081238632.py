from collections import Counter, defaultdict
N, W = map(int, input().split())
wv_dict = defaultdict(list)
for i in range(N):
    w, v = map(int, input().split())
    wv_dict[w] += [v]
sorted_w = sorted(wv_dict.keys())
w0 = sorted_w[0]
w_list = [w0 + i for i in range(4)]
for key in w_list:
    sorted_v = sorted(wv_dict[key], reverse=True)
    for i in range(len(sorted_v)-1):
        sorted_v[i+1] += sorted_v[i]
    wv_dict[key] = [0] + sorted_v
w0, w1, w2, w3 = [w0 + i for i in range(4)]
ans = 0
for c0 in range(len(wv_dict[w0])):
    for c1 in range(len(wv_dict[w0+1])):
        for c2 in range(len(wv_dict[w0+2])):
            for c3 in range(len(wv_dict[w0+3])):
                if w0 * c0 + w1 * c1 + \
                    w2 * c2 + w3 * c3 <= W:
                    v = wv_dict[w0][c0] + wv_dict[w1][c1] + \
                        wv_dict[w2][c2] + wv_dict[w3][c3]
                    ans = max(ans, v)

print(ans)