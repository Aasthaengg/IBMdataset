n = int(input())
p = [int(input()) for _ in range(n)]
high = max(p)
sum = sum(p) - high
high = high // 2
print(sum+high)
