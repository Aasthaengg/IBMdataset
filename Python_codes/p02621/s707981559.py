a = int(input().rstrip())
ans = lambda a: int(a + a**2 + a**3)
print(ans(a))