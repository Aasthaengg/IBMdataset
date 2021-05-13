N, W = map(int, input().split(' '))

import collections
w_v_pairs = collections.defaultdict(list)
for _ in range(N):
    w, v = map(int, input().split(' '))
    w_v_pairs[w].append(v)


for w in w_v_pairs.keys():
    w_v_pairs[w].sort(reverse=True)

ans = 0
weights = list(w_v_pairs.keys())
buf = [(W, 0, 0)]
while len(buf) != 0:
    rest_w, i_weights, v = buf.pop()
    ans = max(ans, v)

    if i_weights < len(weights):
        buf.append((rest_w, i_weights + 1, v))

        w = weights[i_weights]
        values = w_v_pairs[w]
        j = 0
        while j < len(values):
            rest_w -= w
            if rest_w < 0:
                break
            else:
                v += values[j]
                buf.append((rest_w, i_weights+1, v))
                j += 1



# print(w_v_pairs)
print(ans)

