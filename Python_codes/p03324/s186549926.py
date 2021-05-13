D, N = map(int, input().split())
print(int(str(N) + '00' * D) if N != 100 else int(str(N + 1) + '00' * D))
