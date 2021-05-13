H, W = map(int, input().split())
ans = [input() for _ in range(H)]
print("#" * (W + 2))
[print("#" + row + "#") for row in ans]
print("#" * (W + 2))
