N, W = map(int, input().split())
w = []
v = []
for i in range(N):
    wi, vi = map(int, input().split())
    w.append(wi)
    v.append(vi)
ww = [w[0], w[0]+1, w[0]+2, w[0]+3]
d = {}
for i in range(4):
    d[ww[i]] = []
for i in range(N):
    d[w[i]].append(v[i])
for i in range(4):
    d[ww[i]] = sorted(d[ww[i]], reverse=True)
    
ans = 0
for i in range(N+1):
    if len(d[ww[0]]) < i:
        # print('break i: {}'.format(i))
        break
    for j in range(N+1):
        if i + j > N or len(d[ww[1]]) < j:
            # print('break i, j: {}, {}'.format(i, j))
            break
        for k in range(N+1):
            if i + j + k > N or len(d[ww[2]]) < k:
                # print('break i, j, k: {}, {}, {}'.format(i, j, k))
                break
            for l in range(N+1):
                # print(ww[0] * i + ww[1] * j + ww[2] * k + ww[3] * l)

                if i + j + k + l > N or\
                        len(d[ww[3]]) < l or\
                        ww[0] * i + ww[1] * j +\
                        ww[2] * k + ww[3] * l > W:
                    # print('break i, j, k: {}, {}, {}, {}'.format(i, j, k, l))
                    break

                av = sum([d[ww[0]][p] for p in range(i)])
                bv = sum([d[ww[1]][p] for p in range(j)])
                cv = sum([d[ww[2]][p] for p in range(k)])
                dv = sum([d[ww[3]][p] for p in range(l)])
                ans = max(ans, av+bv+cv+dv)
print(ans)


