n, k, q = map(int, input().split())
a = [int(input()) - 1 for i in range(q)]
ans = [k-q]*n
for i in range(q):
    ans[a[i]] += 1
for i in range(n):
    if ans[i] > 0:
        print('Yes')
    else:
        print('No')
