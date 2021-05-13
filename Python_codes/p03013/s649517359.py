n, m = map(int, input().split())

a = []
for _ in range(m):
    a.append(int(input()))
a.append(n+1)

def solve(a,n,m):
    for i in range(len(a)-1):
        if a[i+1] == a[i] + 1:
            return 0

    a_diff = [a[0]-1]
    for i in range(1, m+1):
        a_diff.append(a[i] - a[i-1] - 2)
    ans = 1
    for y in a_diff:
        if y == 0 or y == 1:
            continue
        ans *= count_way(y)
    return ans

def count_way(n):
    memo = [0]*(n+1)
    memo[0] = 1
    memo[1] = 1
    for j in range(n-1):
        memo[j+2] = memo[j+1] + memo[j]
    return memo[n]

print(solve(a,n,m)%1000000007)
