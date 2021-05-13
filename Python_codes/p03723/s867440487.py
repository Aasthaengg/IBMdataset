A, B, C = [int(x) for x in input().split()]
ans = 0
while True:
    if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
        break
    elif A == B == C:
        ans = -1
        break
    ans += 1
    A, B, C = (B + C) // 2, (A + C) // 2, (A + B) // 2

print(ans)