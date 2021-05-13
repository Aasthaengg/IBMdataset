A, B, C = input().split(" ")
A, B, C = int(A), int(B), int(C)
ans = 0
while True:
    if A % 2 != 0 or B % 2 != 0 or C % 2 != 0:
        print(ans)
        break
    if A == B and B == C:
        print(-1)
        break
    A, B, C = (B + C) / 2,  (C + A) / 2, (A + B) / 2
    ans += 1