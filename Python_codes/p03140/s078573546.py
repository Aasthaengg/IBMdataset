N = int(input())
A = input()
B = input()
C = input()
count = 0
for num in range(N) :
    count += len(list(set(list( [ A[num], B[num], C[num] ] ) ) )) - 1
print(count)