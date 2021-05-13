n, m = map(int, input().split())

time_of_try = 100 * (n-m) + 1900 * m
count_of_try = 2 ** m

ans = time_of_try * count_of_try
print(ans)