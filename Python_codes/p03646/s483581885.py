k = int(input())
d, m = divmod(k, 50)

ans = [49 + d for _ in range(50)]

for i in range(m):
    ans = [a - 1 for a in ans]
    ans[i] += 1 + 50

print(50)
print(*ans)