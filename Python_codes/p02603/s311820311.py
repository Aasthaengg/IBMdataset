def solve(n, a):
    ans = 1000
    for i in range(n-1):
        if a[i] < a[i+1]:
            ans += (ans // a[i]) * (a[i+1] - a[i])
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))