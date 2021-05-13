X, A, B = map(int, input().split())
expired = B - A
print("delicious" if expired <= 0 else "safe" if expired <= X else "dangerous")