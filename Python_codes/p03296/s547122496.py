def solve(n, a):
    ans = 0
    for i in range(1, n):
        if a[i-1] == a[i]:
            a[i] *= -1
            ans += 1
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))