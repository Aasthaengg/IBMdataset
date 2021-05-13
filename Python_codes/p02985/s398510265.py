mod = 10 ** 9 + 7
n, k = map(int, input().split())
if n == 1:
    print(k)
    quit()

ans = k * (k - 1)
branch_n = [0] * n
for _ in range(n-1):
     nodes = map(lambda x : int(x) - 1, input().split())
     for i in nodes:
        branch_n[i] += 1
        if branch_n[i] > 1:
            ans = ans * (k - branch_n[i]) % mod
print(ans)