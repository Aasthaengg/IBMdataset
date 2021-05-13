n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0
beforeKill = 0
for i in range(n):
    kill1 = min(A[i] - beforeKill, B[i])
    kill2 = min(A[i+1], B[i] - kill1)
    cnt += kill1 + kill2
    beforeKill = kill2
print(cnt)