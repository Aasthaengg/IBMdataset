def solve(n, x, l):
    p = sorted([(a+b, a-b) for a, b in zip(x, l)])
    _, th = p[0]
    best = 0
    for t, s in p:
        if th <= s:
            best += 1
            th = t
    return best

n = int(input())
x = [0]*n
l = [0]*n
for i in range(n):
    x[i], l[i] = map(int, input().split())
print(solve(n, x, l))