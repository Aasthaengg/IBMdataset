n = int(input())
costs = [int(input()) for _ in range(5)]
nums = [0] * 6
mc = min(costs)
counts = -(-n//mc)
print(counts+4)