k = int(input())
n = 50
b,c = k % n, k // n
ans = [n + c] * (b) + [n + c - b - 1] * (n - b)
print(n)
print(*ans)