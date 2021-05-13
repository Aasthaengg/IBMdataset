N_MAX = 1000000000

n = int(input())
S = list(map(int, input().rstrip().split(" ")))

mergeCnt = 0

def merge(A, left, mid, right):
    
    global mergeCnt
    
    n1 = mid - left
    n2 = right - mid
    
    L = A[left:mid]
    R = A[mid:right]
    
    L.append(N_MAX)
    R.append(N_MAX)
    
    i = j = 0
    
    for k in range(left, right):
        mergeCnt += 1
        if(L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, left, right):
    if (left + 1 < right):
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

if(__name__ == '__main__'):
    
    left = 0
    right = n
    
    mergeSort(S, left,right)
    
    print(*S)
    print(mergeCnt)
