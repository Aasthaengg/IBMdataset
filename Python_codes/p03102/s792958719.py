N,M,C = map(int,list(input().split()))
B = list(map(int,(input().split())))
counter = 0
for i in range(N):
    A = list(map(int,(input().split())))
    sum_val = 0
    for j in range(M):
        sum_val +=A[j]*B[j]
    sum_val += C
    if sum_val >0:
        counter += 1
print(counter)
