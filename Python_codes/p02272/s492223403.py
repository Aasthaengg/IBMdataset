def merge(A, left, mid, right):
    global counter
    INFTY = 10 ** 10
    L = A[left:mid]
    R = A[mid:right]
    L.append(INFTY)
    R.append(INFTY)
    i, j = 0, 0
    for k in range(left, right):
        counter += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)
        
n = int(input())
A = list(map(int, input().split()))

counter = 0
merge_sort(A, 0, n)
print(' '.join(str(a) for a in A))
print(counter)
