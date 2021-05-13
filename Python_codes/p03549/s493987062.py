n, m = map(int, input().split())
ex_times = 1 / ((1 / 2) ** m)
result = (100 * (n - m) + 1900 * m) * ex_times
print(int(result))