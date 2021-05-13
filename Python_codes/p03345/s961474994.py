a, b, c, k = map(int, input().split())
cons = (-1)**k
ans = (a - b) * cons

if abs(ans) > 10**18:
    print("Unfair")
else:
    print(ans)