q, h, s, d = map(int, input().split())
n = int(input())
Q, R = divmod(n, 2)
ans = Q*min([8*q, 4*h, 2*s, d]) + R*min([4*q, 2*h, s])
print(ans)
