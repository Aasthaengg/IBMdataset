def solve(n, a):
    a = sorted(a)
    total = 0
    optimal = 0
    for i in range(n-1):
        total += a[i]
        if total * 2 < a[i+1]:
            optimal = i+1
    return n - optimal

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
