h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
b = [0 for _ in range(n)]
b[0] = a[0]
for i in range(1, n):
    b[i] = b[i - 1] + a[i]
ans = [[0 for _ in range(w)] for _ in range(h)]
c, k, m = 0, 0, 0
for i in range(h):
    for j in range(w):
        c += 1
        if b[k] < c:
            k += 1
        if i % 2 == 0:
            ans[i][j] = k + 1
        else:
            ans[i][w - j - 1] = k + 1

for i in range(h):
    print(" ".join(map(str, ans[i])))