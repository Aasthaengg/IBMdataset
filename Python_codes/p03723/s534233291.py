A, B, C = map(int, input().split())
cnt = 0
while True:
    if A % 2 != 0 or B % 2 != 0 or C % 2 != 0:
        print(cnt)
        break
    elif A == B and A == C:
        print(-1)
        break
    else:
        A, B, C = (B+C)//2, (C+A)//2, (A+B)//2
        cnt += 1