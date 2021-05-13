N, D = map(int, input().split())

w = 2*D + 1

ans = (N + (w - 1)) // w

print(ans)
