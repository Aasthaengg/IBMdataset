n = int(input())
a = list(map(int, input().split()))

l = len(bin(max(a))[2:])

cumsums = [[0] for _ in range(l)]
for i in range(n):
    for j in range(l):
        if a[i] & (1 << j):
            cumsums[j].append(cumsums[j][-1] + 1)
        else:
            cumsums[j].append(cumsums[j][-1])

ans = 0
left = 0
for i in range(1, n+1):
    while left < i:
        f = True
        for j in range(l):
            if cumsums[j][left] < cumsums[j][i] - 1:
                f = False

        if f:
            break
        else:
            left += 1

    ans += i - left
print(ans)
