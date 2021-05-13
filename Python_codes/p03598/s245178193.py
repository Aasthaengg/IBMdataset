N = int(input())
K = int(input())
x = list(map(int, input().split()))
c = 0
for xi in x:
    c += min(2 * xi, 2 * abs(K - xi))
print(c)