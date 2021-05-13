n = int(input())
A = [int(input())for _ in range(n)]
if A[0] != 0:
    print(-1)
    exit()

ans = A[-1]
for a, prev_a in reversed(tuple(zip(A, A[1:]))):
    if a == prev_a-1:
        continue
    if a < prev_a-1:
        print(-1)
        break
    ans += a
else:
    print(ans)
