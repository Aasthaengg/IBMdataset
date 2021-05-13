n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]
p = [0] * n

for ai in a:
    p[ai-1] += 1

ans = 0
for pi in p:
    if k-q+pi > 0:
        print('Yes')
    else:
        print('No')
