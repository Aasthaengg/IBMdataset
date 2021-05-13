X, Y, A, B, C = map(int, input().split())
p = sorted(map(int, input().split()), reverse=True)[:X]
q = sorted(map(int, input().split()), reverse=True)[:Y]
r = list(map(int, input().split()))

ans = sum(sorted(p+q+r, reverse=True)[:X+Y])
print(ans)