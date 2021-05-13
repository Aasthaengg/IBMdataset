A, B, C = map(int, input().split())

count = 0
while True:
    if A % 2 != 0 or B % 2 != 0 or C % 2 != 0:
        break
    a = B // 2 + C // 2
    b = C // 2 + A // 2
    c = A // 2 + B // 2
    if a == A and b == B and c == C:
        print(-1)
        exit()
    A = a
    B = b
    C = c
    count += 1

print(count)
