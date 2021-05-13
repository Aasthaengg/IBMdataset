a, b, c, k = map(int, input().split())

if k % 2 == 0:
    ans = a - b

else:
    ans = b - a

print(ans if 10 ** 18 >= ans else 'Unfair')