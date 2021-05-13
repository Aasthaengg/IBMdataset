def solve(n, m, a, b):
    D = {(i+1): 0 for i in range(n)}
    for v in a + b:
        D[v] += 1
    ok = len(list(
        filter(lambda num: num % 2 == 0, D.values())
    )) == n
    return "YES" if ok else "NO"

n, m = map(int, input().split())
ab = [map(int, input().split()) for i in range(m)]
a, b = zip(*ab)
print(solve(n, m, a, b))