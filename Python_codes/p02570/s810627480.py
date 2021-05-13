def solve(d, t, s):
    return "Yes" if d <= t*s else "No"

d, t, s = map(int, input().split())
print(solve(d, t, s))