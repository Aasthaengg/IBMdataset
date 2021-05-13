(n, a, b) = map(int, input().split())

ans_max = min(a, b)
ans_min = max(0, a + b - n)
print("{} {}".format(ans_max, ans_min))
