N, X = [int(i) for i in input().split()]
donut_type = [int(input()) for i in range(N)]
X = X - sum(donut_type)
result = N + X // min(donut_type)

print(result)