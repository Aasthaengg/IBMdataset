N = int(raw_input())
A = map(int, raw_input().split())
count = 0
flag = True
while flag:
    flag = False
    for j in range(N-1, 0, -1):
        if A[j] < A[j-1]:
            A_j = A[j]
            A[j] = A[j-1]
            A[j-1] = A_j
            flag = True
            count += 1
print " ".join(map(str, A))
print count