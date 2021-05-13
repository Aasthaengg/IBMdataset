N = int(input())
S = [0]*N
sm = 0
A = list(map(int,input().split()))
for i in range(N):
    ai = A[i]
    sm += ai
    S[i] = sm
score = 0
min_score = float("inf")
for i in range(N-1):
    score = abs(S[i]-(S[N-1]-S[i]))
    min_score = min(score,min_score)
print(min_score)

