n, k = [int(input()) for _ in range(2)]
x = list(map(int, input().split()))

print(sum([min(x[i], abs(x[i] - k)) * 2 for i in range(n)]))
