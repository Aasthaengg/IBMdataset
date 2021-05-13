A, B, C = map(int,input().split())

if B %2 != 0:
    print(0)
    exit()
if A == B == C:
    print(-1)
    exit()

x = B/2
cnt = 0
while A % 2 == 0 and C % 2 == 0:
    tmp_a = A
    tmp_c = C
    A = tmp_c/2 + x
    C = tmp_a/2 + x
    cnt += 1
print(cnt)