


N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

if A[0] != 0:
    print(0)
    exit()


ans = 1
colors = [0] * 3
for n in A:
    ans *= colors.count(n)
    ans %= MOD
    for i in range(3):
        if colors[i] == n:
            colors[i] += 1
            break
print(ans)
