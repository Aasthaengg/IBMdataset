n, k, *W = map(int, open(0).read().split())
left, right = 1000000000, max(W) - 1


def check(M):
    L = [W[0]]
    for i in range(1, n):
        if L[-1] + W[i] <= M:
            L[-1] += W[i]
        else:
            L.append(W[i])
    return len(L) <= k


while left - right > 1:
    m = (left + right) // 2
    if check(m):
        left = m
    else:
        right = m
print(left)

