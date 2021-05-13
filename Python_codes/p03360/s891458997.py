a, b, c = map(int, input().split())
K = int(input())
m = max(a, b, c)
print(a + b + c - m + m * 2 ** K)