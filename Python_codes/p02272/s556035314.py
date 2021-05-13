import sys
count = 0

def merge(A, left, mid, right):
    global count
    L = A[left:mid]
    R = A[mid:right]
    L.append(sys.maxint)
    R.append(sys.maxint)
    i = 0
    j = 0
    for k in xrange(left, right):
        count += 1
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

n = int(raw_input())
S = map(int, raw_input().split())
mergeSort(S, 0, n)
print ' '.join(map(str, S))
print count