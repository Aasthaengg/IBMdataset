n, a, b = map(int, input().split())
c = a + b

rep = n // c
ans = a * rep + min(a, n-c*rep)

print(ans)