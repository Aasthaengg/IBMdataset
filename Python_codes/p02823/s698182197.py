N, A, B = map(int, input().split())
if abs(A - B) % 2 == 0:
    print(abs(A - B) // 2)
else:
    print(min(min(A, B) + abs(A - B) // 2, N - max(A, B) + 1 + abs(A - B) //2))
