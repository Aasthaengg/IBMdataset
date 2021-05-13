N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = [A[i]-B[i] for i in range(N)]
if sum(A) < sum(B):
    print(-1)
    exit()
C.sort()
d = 0
ans = 0
for c in C:
    if c >= 0:
        break
    d += c
    ans += 1
C.reverse()
for i in range(N):
    if d >= 0:
        break
    d += C[i]
    ans += 1
print(ans)