A, B = map(int, input().split())

slot = 1
tap = 0
while slot < B:
    slot += A-1
    tap += 1
print(tap)
