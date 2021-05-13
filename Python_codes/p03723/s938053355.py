A, B, C = map(int, input().split())

if A == B == C and A%2==0:
    print(-1)
else:
    cnt = 0
    while A%2 == B%2 == C%2 == 0:
        x = (B+C)//2
        y = (A+C)//2
        z = (A+B)//2
        A = x
        B = y
        C = z
        cnt += 1
    print(cnt)