def solve(n, a, b):
    v = sorted(zip(a, b), key=lambda x:x[0]+x[1], reverse=True)
    return sum(x+y for x, y in v[::2]) - sum(b)

n = int(input())
a = [0]*n
b = [0]*n
for i in range(n):
    a[i], b[i] = map(int, input().split())
print(solve(n, a, b))