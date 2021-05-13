n = int(input())
A = list(map(int, input().split()))

A.sort()

for i in range(len(A)):
    if i == 0:
        continue
    if A[i-1] == A[i]:
        print('NO')
        exit()
print('YES')
