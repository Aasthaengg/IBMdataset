def solve(n, h, w, a, b):
    ans = 0
    for i in range(n):
        if (a[i] >= h) and (b[i] >= w):
            ans += 1
    return ans

n, h, w = map(int, input().split())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
print(solve(n, h, w, a, b))