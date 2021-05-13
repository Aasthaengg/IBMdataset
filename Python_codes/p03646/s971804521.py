K = int(input())

N = 50
ans = [49] * N

ans = [a + (K // 50) - (K % 50) for a in ans]
for i in range(K % 50):
    ans[i] += (K % 50) + 1

print(N)
print(*ans, sep=' ')
