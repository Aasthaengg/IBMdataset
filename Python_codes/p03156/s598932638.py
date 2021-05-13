def solve(n, a, b, p):
    v = [0] * 3
    for i in range(n):
        if p[i] <= a:
            v[0] += 1
        elif p[i] <= b:
            v[1] += 1
        else:
            v[2] += 1
    return min(v)

n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
print(solve(n, a, b, p))