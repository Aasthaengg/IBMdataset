n = int(input())
S = [*map(int, input().split())]

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    
    L = list(range(n1+1))
    R = list(range(n2+1))
    
    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]
        
    L[n1] = 100000000000
    R[n2] = 100000000000
    
    i = 0
    j = 0
    
    for k in range(left, right):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
            
        else:
            A[k] = R[j]
            j = j + 1
            
    return right - left
            
def mergeSort(A, left, right):
    count = 0
    if left+1 < right:
        mid = int((left + right) / 2)
        count += mergeSort(A, left, mid) + mergeSort(A, mid, right)
        count += merge(A, left, mid, right)

    return count

count = mergeSort(S, 0, n)
print(*S)
print(count)
