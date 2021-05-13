a, b, c = map(int, input().split())
poison_eaten = min(a + b + 1, c)
print(b + poison_eaten)
