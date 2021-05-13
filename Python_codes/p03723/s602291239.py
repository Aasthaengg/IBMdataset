A, B, C = map(int, input().split())

cnt = 0
if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
    print(cnt)
elif A == B == C:
        cnt = -1
        print(cnt)
else:
    while True:
        a, b, c = A, B, C
        if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
            break
        A, B, C = (b + c) / 2, (a + c) / 2, (a + b) / 2
        cnt += 1
    
    print(cnt)