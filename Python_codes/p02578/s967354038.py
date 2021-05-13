N = int(input())
A = list(map(int, input().split()))

MAX = 0
ANS = 0

for i in range(N):
    ANS += max(0, MAX - A[i])
    MAX = max(MAX, A[i])

print(ANS)