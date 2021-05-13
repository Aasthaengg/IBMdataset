N, K = map(int, input().split())
A = list(map(int, input().split()))
memo = [0] * N
ans = 0

for a in A:
    memo[a-1] += 1
    
memo.sort()

for i in memo[:N-K]:
    ans += i

print(ans)
