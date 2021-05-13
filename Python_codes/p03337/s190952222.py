a, b = map(int, input().split())
result = []
result.append(a+b)
result.append(a-b)
result.append(a*b)
print(max(result))