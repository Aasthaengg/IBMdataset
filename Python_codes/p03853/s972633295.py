#ABC 049 B - たてなが
H, W = map(int, input().split())
result = [""] * (H*2)
for i in range(H):
    C = input()
    for j in range(W):
        result[2 * i] = C
        result[2 * i + 1] = C
for i in range(H * 2):
    print(result[i])