H, W = map(int, input().split())
C = []
for _ in range(H):
    c = input()
    C.append(c)
    C.append(c)
print(*C, sep='\n')