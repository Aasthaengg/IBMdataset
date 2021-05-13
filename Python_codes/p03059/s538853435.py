a, b, t = map(int, input().split())
print(b * sum(1 for _ in range(a, t+1, a)))
