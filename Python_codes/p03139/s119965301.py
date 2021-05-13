n, a, b = map(int, input().split())
both_max = min(a, b)
if a+b <= n:
    both_min = 0
else:
    both_min = a+b-n
print(both_max, both_min)