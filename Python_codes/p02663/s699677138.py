H1, M1, H2, M2, K = [int (x) for x in input().split()]

M3 = (H2 * 60 + M2) - (H1 * 60 + M1)
T = M3 - K
print(T)