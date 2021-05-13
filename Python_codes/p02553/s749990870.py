a, b, c, d = map(int, input().split())

result = [i * j for i in [a, b] for j in [c, d]]
print(max(result))