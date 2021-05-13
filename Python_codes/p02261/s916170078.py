def BubbleSort(C, N):
    for i in range(N):
        for j in range(N - 1, i, -1):
            if C[j][1] < C[j - 1][1]:
                C[j], C[j - 1] = C[j - 1], C[j]
def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i + 1, N):
            if C[j][1] < C[minj][1]:
                minj = j
        if i != minj:
            C[i], C[minj] = C[minj], C[i]
N = int(input())
A = input().split()
B = A[:]
C = A[:]
BubbleSort(B, N)
print(*B)
print("Stable")
SelectionSort(C, N)
print(*C)
print("Stable" if B == C else "Not stable")
