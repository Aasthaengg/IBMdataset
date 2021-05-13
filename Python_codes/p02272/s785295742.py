def merge(A, left, mid, right):
    global c
    L=A[left:mid]+[1e10]
    R=A[mid:right]+[1e10]
    i=j=0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        c+=1
def mergeSort(A, left, right):
    if left+1 < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)
c=0
n=int(input())
A=list(map(int,input().split()))
mergeSort(A, 0, n)
print(*A)
print(c)
