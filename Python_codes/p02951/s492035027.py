A, B, C = map(int, input().split())
print(0 if A - B >= C else C - A + B)