N, C, K, *T = map(int, open(0).read().split())
T = sorted(T)
ans = 0
curr = [T[0]]
for i in range(N - 1):
    if len(curr) < C and T[i + 1] - curr[0] <= K:
        curr.append(T[i + 1])
    else:
        ans += 1
        curr = [T[i + 1]]
print(ans + 1)
