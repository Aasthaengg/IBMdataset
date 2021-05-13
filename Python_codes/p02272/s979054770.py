SENTINEL = 2000000000
L = R = [0]
cnt = 0
def merge(A, n, left, mid, right):
    L = A[left:mid] + [SENTINEL]
    R = A[mid:right] + [SENTINEL]
    i = j = 0
    global cnt
    for k in range(left, right):
        cnt += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
def mergeSort(A, n, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A, n, left, mid)
        mergeSort(A, n, mid, right)
        merge(A, n, left, mid, right)
n = int(input())
A = [int(i) for i in input().split()]
mergeSort(A, n, 0, n)
print(*A)
print(cnt)