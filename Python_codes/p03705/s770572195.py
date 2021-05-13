n, a, b = map(int, input().split())
if a > b or (n == 1 and a != b):
    print(0)
    exit()
m = a * (n - 1) + b
M = a + b * (n - 1)
print(M - m + 1)
