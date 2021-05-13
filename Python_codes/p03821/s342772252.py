n = int(input())
a, b = [], []
ans = 0


def solve(x, y):
    n = -(-x//y)
    return (y)*n-x


for _ in range(n):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)

for i in reversed(range(n)):
    ans += solve(a[i]+ans, b[i])

print(ans)
