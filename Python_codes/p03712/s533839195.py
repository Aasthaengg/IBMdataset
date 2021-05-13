H, W = map(int, input().split())

print("#" * (W + 2))
for _ in range(H):
    line = input()
    print(f"#{line}#")
print("#" * (W + 2))