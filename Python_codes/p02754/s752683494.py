n, a, b = map(int, input().split())
ans1, ans2 = divmod(n, a+b)
print(ans1 * a + min(ans2, a))