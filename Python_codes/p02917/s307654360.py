n = int(input())
b = list(map(int, input().split()))
print(b[0] + b[-1] + sum([min(b[i], b[i + 1]) for i in range(n - 2)]))