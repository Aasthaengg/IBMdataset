import sys
input = sys.stdin.readline
N = int(input())
A = [int(input()) for _ in range(N)]
ans = 0
for i, a in enumerate(A):
    if a > i:
        break
    if i == 0:
        continue
    if a == A[i-1]+1:
        ans += 1
    elif a <= A[i-1]:
        ans += a
    else:
        break
else:
    print(ans)
    exit()
print(-1)
