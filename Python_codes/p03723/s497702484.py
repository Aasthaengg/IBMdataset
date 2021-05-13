A, B, C = map(int, input().split())
if A % 2 == 0 and A == B and B == C:
    print(-1)
    exit()

count = 0
while (A % 2, B % 2, C % 2) == (0, 0, 0):
    A, B, C = (B + C) // 2, (A + C) // 2, (A + B) // 2
    count += 1

print(count)
