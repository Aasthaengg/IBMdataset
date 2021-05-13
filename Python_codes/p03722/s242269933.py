n, m = map(int, input().split())

edges = []
for i in range(m):
    a, b, w = map(int, input().split())
    edges.append((a-1, b-1, w))

init_val = -10 ** 9 * 1000
d = [init_val] * n
d[0] = 0
for _ in range(n):
    updated = False
    for a, b, w in edges:
        if d[a] != init_val and d[b] < d[a] + w:
            d[b] = d[a] + w
            updated = True
    if not updated:
        break
if updated: #閉路の存在
     for a, b, w in edges:
        if d[a] != init_val and d[b] < d[a] + w:
            d[b] = d[a] + w
            if b == n - 1:
                print('inf')
                quit()
print(d[n-1])
