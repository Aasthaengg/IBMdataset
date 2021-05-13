n, k = map(int, input().split())
x = list(map(int, input().split()))

x_neg = []
x_pos = []
for xx in x:
    if xx < 0:
        x_neg.append(-xx)
    else:
        x_pos.append(xx)
x_neg = x_neg[::-1]

ans = float('inf')
if k <= len(x_neg):
    ans = min(ans, x_neg[k-1])
if k <= len(x_pos):
    ans = min(ans, x_pos[k-1])

for i in range(1, k):
    j = k - i
    if i <= len(x_pos) and 1 <= j <= len(x_neg):
        d1 = x_pos[i - 1]
        d2 = x_neg[j - 1]
        d = min(d1, d2) * 2 + max(d1, d2)
        ans = min(ans, d)
print(ans)
