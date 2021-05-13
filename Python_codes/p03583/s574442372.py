import sys

n = int(input())

for i in range(1, 3500):
    for j in range(1, 3500):
        rest = 4 * i * j - (i + j) * n
        if rest > 0:
            ans = n * i * j / rest
            if ans.is_integer():
                print(i, j, int(ans))
                sys.exit()