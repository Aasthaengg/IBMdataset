n, k = map(int, input().split())
arr = input()

# ランレングス圧縮
compressed = []
curr = ""
for x in arr:
    if curr != x:
        compressed.append(x)
        curr = x

# 境界の個数はランレングス圧縮後の文字数 - 1
boundary = len(compressed) - 1

# 2個ずつ圧縮可能
x = max(0, boundary - 2 * k)

print(n - 1 - x)