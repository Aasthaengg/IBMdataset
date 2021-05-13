input()
b = list(map(int, input().split()))
ans = sum(min(i, j) for i, j in zip(b[1:], b[:-1]))
print(b[0] + ans + b[-1])