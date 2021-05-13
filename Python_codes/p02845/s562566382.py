N = int(input())
A = list(map(int, input().split()))
Ans = [0] * (N+1)
mod = 1000000007
Ans[0] = 3
ans = 1
for a in A:
    a += 1
    ans *= Ans[a-1]
    ans %= mod
    Ans[a-1] -= 1
    Ans[a] += 1

print(ans % mod)



