A = list(map(int,input().split()))
A.sort()
answer = 0
for i in range(len(A)):
    if i != 0:
        answer = answer + (A[i] - A[i - 1])
print(answer)