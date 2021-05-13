# 2020/07/27
# エイシング プログラミング コンテスト 2020 - C

# Input
n = int(input())
alist = [0] * (n + 1)

# Calc
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            calc_n = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if calc_n <= n:
                alist[calc_n] = alist[calc_n] + 1
            else:
                break

# Output
for i in range(1, n+1):
    print(alist[i])
