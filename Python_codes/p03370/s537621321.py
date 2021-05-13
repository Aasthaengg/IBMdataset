N, X = [int(i) for i in input().split()]
donut_type = [int(input()) for i in range(N)]
X = X - sum(donut_type)
result = N
while X >= sorted(donut_type)[0]:
    X = X - sorted(donut_type)[0]
    result += 1

print(result)