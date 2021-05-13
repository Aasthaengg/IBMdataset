n = int(input())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]
c = sorted(a)
d = sorted(b)

ans = 0
if n % 2 == 1:
    ans = d[(n-1)//2] - c[(n-1)//2] + 1
else:
    ans = d[n//2] + d[n//2 - 1] - c[n//2] - c[n//2 - 1] + 1

print(ans)