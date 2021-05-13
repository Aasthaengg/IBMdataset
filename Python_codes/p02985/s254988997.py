# coding: utf-8
# Your code here!

n,k = map(int,input().split())

tree = [[] for i in range(n)]

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

kouho = [0]
used_tree = [0 for i in range(n)]
used_tree[0] = 1
ans = k
while kouho:
    head = kouho.pop()
    if head == 0:
        start = k-1
    else:
        start = k-2
    for tail in tree[head]:
        if used_tree[tail] == 0:
            ans *= start
            ans %= 1000000007
            start -= 1
            used_tree[tail] = 1
            kouho.append(tail)
print(ans)