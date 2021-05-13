N, X, T = map(int, input().split())

per = int(N/X) if N % X == 0 else int(N/X) + 1
print(T * per)