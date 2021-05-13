n, x = map(int, input().split())
m = [int(input()) for _ in range(n)]
x -= sum(m)
ans = n
m.sort()
ans += x // m[0]
print(ans)