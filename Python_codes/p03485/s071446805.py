A, B = map(int, input().split())
AB = A+B
if AB % 2 == 0:
    print((AB) // 2)
else:
    print((AB) // 2 + 1)
