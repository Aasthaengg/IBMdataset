cnt = 0

def merge(A, left, mid, right):
    global cnt
    L, R = A[left:mid], A[mid:right]
    L.append(float('inf'))
    R.append(float('inf'))

    i, j = 0, 0

    for k in range(left, right):
        cnt += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, left, right):
    if left+1 < right:
        mid = (left + right) / 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


def main():
    global cnt
    n = int(raw_input())
    A = map(int, raw_input().split())

    cnt = 0
    merge_sort(A, 0, n);

    print " ".join(map(str, A))
    print cnt


main()