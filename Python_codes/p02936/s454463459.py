n, q = map(int, input().split())
tree = [[] for i in range(n)]
l = [0]*n

for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(q):
    p, x = map(int, input().split())
    p -= 1
    l[p] += x

q = [0]
s = [-1]*n
s[0] = l[0]
while len(q) > 0:
    r = q.pop()
    for i in tree[r]:
        if s[i] == -1:
            s[i] = s[r] + l[i]
            q.append(i)
print(*s)