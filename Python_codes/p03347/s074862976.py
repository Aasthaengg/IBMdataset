import sys
read = sys.stdin.read

N, *A = map(int, read().split())

if A[0] != 0:
    print(-1)
    exit()


answer = 0
A.append(0)
for i in range(N):
    if A[i + 1] - A[i] > 1:
        print(-1)
        exit()
    if A[i + 1] <= A[i]:
        answer += A[i]

print(answer)