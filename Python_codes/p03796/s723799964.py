N = int(input())
n = 1000000007
p = 1
for i in range(1, N + 1):
    p *= i
    p %= n
print(p)
