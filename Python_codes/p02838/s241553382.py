N = int(input())
A = list(map(int, input().split()))

m = 1000000007

result = 0
for i in range(60):
    j = 1 << i
    c = sum((a & j) >> i for a in A)
    result += (c * (N - c)) << i
    result %= m
print(result)
