A, B = map(int, input().split())
k = A + B
print(int(k / 2) if k%2 == 0 else "IMPOSSIBLE")