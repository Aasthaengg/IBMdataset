n = int(input())
a, b = [], []
for i in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
ans = 0
for i in range(n - 1, -1, -1):
    if (a[i] + ans) % b[i] != 0:
        ans += b[i] - ((a[i] + ans) % b[i])
print(ans)