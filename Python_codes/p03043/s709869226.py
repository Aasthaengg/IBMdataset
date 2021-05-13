n, k = map(int, input().split())

# pows[i] = pow(2, i)
pows = [1]
while pows[-1] < k:
    pows.append(2 * pows[-1])

ans = 0
ind = -1
for i in range(1, n + 1):
    if -ind < len(pows) and pows[ind-1] * i >= k:
        ind -= 1
    ans += pows[-ind - 1]

print(ans / (pows[-1] * n))