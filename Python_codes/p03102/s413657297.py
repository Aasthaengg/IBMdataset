N, M, C = map(int, input().split())
B = list(map(int, input().split()))
count = 0
for i in range(N) :
    sum = 0
    A = list(map(int, input().split()))
    for j in range(M) :
        sum += A[j] * B[j]
    if sum + C > 0 :
        count += 1
print(count)
