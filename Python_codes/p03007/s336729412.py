N, *A = map(int, open(0).read().split())

x = sorted([v for v in A if v >= 0])
y = sorted([v for v in A if v < 0], reverse=True)

ans = []
if len(y) == 0:
    cnt = x[0]
    for v in x[1:-1]:
        ans.append((cnt, v))
        cnt -= v
    ans.append((x[-1], cnt))
    print(x[-1] - cnt)
elif len(x) == 0:
    cnt = y[0]
    for v in y[1:]:
        ans.append((cnt, v))
        cnt -= v
    print(cnt)
else:
    for v in x[:-1]:
        ans.append((y[0], v))
        y[0] -= v
        
    cnt = x[-1]
    for v in y:
        ans.append((cnt, v))
        cnt -= v
    print(cnt)
    
for v in ans:
    print(*v)