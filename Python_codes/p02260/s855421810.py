N = int(raw_input())
A = raw_input().split(" ")

count = 0
for i in range(0, N):
    minj = i
    for j in range(i, N):
        if int(A[j]) < int(A[minj]):
            minj = j

    if i != minj:
        temp = A[i]
        A[i] = A[minj]
        A[minj] = temp
        count += 1

print " ".join(A)
print count