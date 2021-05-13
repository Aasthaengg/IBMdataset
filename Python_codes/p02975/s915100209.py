def solve(n, a):
    p = 0
    for x in a:
        p ^= x
    return "Yes" if p == 0 else "No"

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))