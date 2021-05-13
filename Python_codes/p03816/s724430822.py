n = int(input())
a = list(map(int, input().split()))
b = set(a)
print(n - 2 * ((n - len(b) + 1) // 2))