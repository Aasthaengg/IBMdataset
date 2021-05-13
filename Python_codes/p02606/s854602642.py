def solve(l, r, d):
    return r // d - (l-1) // d

l, r, d = map(int, input().split())
print(solve(l, r, d))