
N = int(input())
min = 1000000000

for i in range(1,N):
    A = str(N - i)
    B = str(i)
    temp = 0
    for j in range(len(A)):
        temp += int(A[j])
    for j in range(len(B)):
        temp += int(B[j])
    if min > temp:
        min = temp
print(min)





