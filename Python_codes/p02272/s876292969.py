def merge(A, left, mid, right):
    L = A[left:mid] 
    R = A[mid:right]
        
    L.append(float("inf"))
    R.append(float("inf"))
    
    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    global count
    count += right - left
            
def mergeSort(A, left, right):
    if left+1 < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

n = int(input())
A = list(map(int, input().split(" ")))
count = 0
mergeSort(A, 0, len(A))
print(*A)
print(count)