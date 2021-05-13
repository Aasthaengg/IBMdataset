n, m, x = map(int, input().split())
a = list(map(int, input().split()))

result = min(len([i for i in a if i > x]), len([i for i in a if i < x]))
print(result)
