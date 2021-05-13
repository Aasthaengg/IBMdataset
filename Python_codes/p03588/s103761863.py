n = int(input())
a, b = sorted([tuple(map(int, input().split())) for _ in range(n)])[::-1][0]
print(a + b)