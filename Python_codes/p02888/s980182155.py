import bisect
N = int(input())
L = list(map(int, input().split()))
ans = 0
L.sort()
for a_i in range(N-2):
    for b_j in range(a_i+1, N-1):
        c_idx = bisect.bisect_left(L, L[a_i]+L[b_j])
        if c_idx > b_j:
            ans += c_idx - b_j - 1
print(ans)