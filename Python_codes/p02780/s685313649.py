n, k = map(int, input().split())
p = list(map(int, input().split()))
e = lambda x: 0.5*(x+1)
if k == 1:
    res = e(max(p))
else:
    s = [0]
    s[0] = sum(p[:k])
    for i in range(1, n-k+1):
        s.append(s[i-1] - p[i-1] + p[i+k-1])
    idx = s.index(max(s))
    res = sum([e(p[i]) for i in range(idx, idx+k)])
print(res)