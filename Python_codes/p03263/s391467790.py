h, w = map(int, input().split())
ns = []
for _ in range(h):
    ns.append([i % 2 for i in map(int, input().split())])
ans = []
for i in range(h-1):
    for j in range(w):
        if ns[i][j]:
            ans.append('{} {} {} {}'.format(i+1, j+1, i + 2, j+1))
            ns[i + 1][j] = (ns[i + 1][j] + 1) % 2
for j in range(w - 1):
    if ns[-1][j]:
        ans.append('{} {} {} {}'.format(h, j + 1, h, j + 2))
        ns[-1][j+1] = (ns[-1][j+1]+1) % 2
print(len(ans))
for i in ans:
    print(i)

