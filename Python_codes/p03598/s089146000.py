N = int(input())
K = int(input())
x = tuple(map(int, input().split()))
result = 0
for i in range(N):
    result += min(abs(x[i]), abs(K - x[i]))
print(result * 2)
