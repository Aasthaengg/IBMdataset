n = int(input())
a = list(map(int, input().split()))

# n_C_rの最大化
# nは出来るだけ大きい方が良く、rは出来るだけn/2に近い方が良い

# n>rという条件があるので、サンプル２では(100,100)は許されない
#
x = max(a)
y = float("inf")
for ai in a:
    if abs(x / 2 - ai) < abs(x / 2 - y) and ai < x:
        y = ai
print(x, y)
