A, B = map(int, input().split())
C = sorted([A+B, A-B, A*B], reverse=True)
print(C[0])