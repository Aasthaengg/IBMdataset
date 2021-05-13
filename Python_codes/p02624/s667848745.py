N = int(input())
sho_list = [0] * (N + 1)
for n in range(1, N + 1):
    for j in range(n, N + 1, n):
        sho_list[j] += 1
ans = 0
for k in range(1, N + 1):
    ans += k * sho_list[k]
print(ans)