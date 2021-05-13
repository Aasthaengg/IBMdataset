import sys

cnt = 0

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = range(n1 + 1)
    R = range(n2 + 1)

    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]

    L[n1] = 1000000000
    R[n2] = 1000000000
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

def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) / 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    S = map(int, lines[1].split())
    mergeSort(S, 0, int(lines[0]))
    print " ".join([str(s) for s in S])
    print cnt