N, H, W = [int(_) for _ in input().split()]
AB =[[int(_) for _ in input().split()] for _ in range(N)]
print(sum([1 for a, b in AB if a >= H and b >= W]))