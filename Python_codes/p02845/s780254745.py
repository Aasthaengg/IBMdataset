n = int(input())
A = list(map(int, input().split()))
mod = 10**9 + 7
mem = [0, 0, 0]
ans = 1
for i in range(n):
    ans *= mem.count(A[i])
    ans %= mod
    if ans == 0: break
    idx = mem.index(A[i])
    mem[idx] += 1
print(ans)