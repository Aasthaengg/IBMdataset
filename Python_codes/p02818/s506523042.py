a, b, k = map(int, input().split())
res_a = max(0, a - k)
res_b = b if res_a > 0 else max(0, b - (k - a))
print(f'{res_a} {res_b}')
