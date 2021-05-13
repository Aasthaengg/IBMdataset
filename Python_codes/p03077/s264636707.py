n = int(input())
m = [int(input()) for _ in range(5)]
bottleneck = min(m)
ans = 4 + -(-n // bottleneck)
print(ans)