A, B, C, K = list(map(int, input().split()))

score = 0
if K <= A:
    score = K
    print(score)
    exit()

score += A
K -= A
if K <= B:
    print(score)
    exit()

K -= B
print(score - K)