N = int(input())
K = 1
while K * (K - 1) // 2 <= N:
    if K * (K - 1) // 2 == N:
        break
    K += 1
else:
    print('No')
    exit()

print('Yes')
s = 1
ans = [[] for i in range(K)]
for k in range(K - 1, 0, -1):
    for i in range(k):
        ans[K - k - 1].append(s + i)
        ans[K - k + i].append(s + i)
    s += k

print(K)
for i in range(K):
    ans[i].insert(0, len(ans[i]))
    print(*ans[i])

