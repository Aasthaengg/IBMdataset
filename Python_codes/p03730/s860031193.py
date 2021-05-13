A, B, C = map(int, input().split())
ans = False
for i in range(A, A*B+A, A):
    if i % B == C:
        ans = True
        break
if ans:
    print('YES')
else:
    print('NO')
