A, B, C = map(int, input().split(" "))
doku = min(A + B + 1, C)
print(doku + B)