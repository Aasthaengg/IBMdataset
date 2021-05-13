N = int(input())
a = sorted(list(map(int, input().split())),reverse=True)
A = 0
for i in range(1, 2 * N, 2):
    A += a[i]
print(A)