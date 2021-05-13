A,B,C = map(int, input().split())
cnt = 0
if A%2 or B%2 or C%2:
    print(cnt)
    exit()
if A == B and B == C:
    print(-1)
    exit()
while True:
    if A%2 or B%2 or C%2:
        print(cnt)
        break
    temp_a = A//2
    temp_b = B//2
    temp_c = C//2
    A += 2*temp_a + temp_b + temp_c
    B += 2*temp_b + temp_a + temp_c
    C += 2*temp_c + temp_a + temp_b
    cnt += 1