import math
N = int(input())
A = list(map(int,input().split()))
A.sort(reverse = True)
score = A[0]
for i in range(1, math.ceil(N*0.5)):
    if N - i * 2 != 1:
        score += 2 * A[i]
    else:
        score += A[i]
print(score)