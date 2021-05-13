a,b = map(int, input().split())

_l = list([a+a-1, b+b-1, a+b])

ans = max(_l)

print(ans)