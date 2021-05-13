import sys
A, B, C = map(int, input().split())
ans = 0

if A == B == C and not A == 1:
    print(-1)
    sys.exit()

while True:
    if A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        t_A, t_B, t_C = A, B, C
        A = (t_B + t_C) // 2
        B = (t_C + t_A) // 2
        C = (t_A + t_B) // 2
        ans += 1
    else:
        print(ans)
        break