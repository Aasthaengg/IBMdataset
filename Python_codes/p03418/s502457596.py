import math

def count(n, k, b):
    if k >= b:
        return 0
    n_blocks = math.floor((n+1) / b)
    ans = (b-k) * n_blocks

    remainder = (n+1) - n_blocks * b
    if remainder > k:
        ans += remainder - k

    #print(f'b={b}, ans={ans}, n_blocks={n_blocks}, remainder={remainder}')
    return ans

n, k = map(int, input().split())

if k == 0:
    print(n*n)
    exit(0)

ans = 0
for b in range(1, n+1):
    cnt = count(n, k, b)
    ans += cnt
    #print(f'b={b}, cnt={cnt}, n={n}, k={k}')
print(ans)
