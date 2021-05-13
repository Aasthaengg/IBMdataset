import sys
n, k = map(int, input().split())

if k % 2 == 1:
    print((n // k)**3)
    sys.exit()

# 偶数の時は初項が1/2、公差kの数列から選べる
x = (n - k // 2) // k + 1

print((n // k)**3 + x**3)