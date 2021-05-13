N = int(input())
K = int(input())
x_list = list(map(int, input().split()))

res = 0
for xi in x_list:
    res += 2 * min(xi, (K-xi))
print(res)
