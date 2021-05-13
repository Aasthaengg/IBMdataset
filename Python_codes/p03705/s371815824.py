n, a, b = map(int,input().split())
num = b - a + 1

ans = b*(n-2) - a*(n-2) + 1 if b >= a else 0
print(ans if ans >= 0 else 0)