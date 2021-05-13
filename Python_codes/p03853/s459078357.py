H, W = map(int, input().split())
C = [input() for _ in range(H)]
print("\n".join(c + "\n" + c for c in C))