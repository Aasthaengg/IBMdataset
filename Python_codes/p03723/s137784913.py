A, B, C = map(int, input().split())
cnt = 0

if A == B == C and A % 2 == 0:
    cnt = -1
else:
    while A%2 == 0 and B%2 == 0 and C%2 == 0:
        A, B, C = int((B+C)/2), int((A+C)/2), int((A+B)/2)
        cnt += 1

print(cnt)