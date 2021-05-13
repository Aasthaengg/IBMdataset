num = int(input())
arr = list(map(int, input().split()))

def merge(arr, left, middle, right, count):
    L = arr[left:middle]
    L.append(float('inf'))
    R = arr[middle:right]
    R.append(float('inf'))

    iterL, iterR = iter(L), iter(R)
    l,r = next(iterL), next(iterR)

    for index in range(left, right):
        count += 1
        if l <= r:
            arr[index] = l
            l = next(iterL)
        else:
            arr[index] = r
            r = next(iterR)
    return count

def merge_sort(arr, left, right, count):

    if left + 1 < right:
        pivot = (left + right) // 2
        count = merge_sort(arr, left,  pivot, count)
        count = merge_sort(arr, pivot, right, count)

        count = merge(arr, left, pivot, right, count)
    return count

count = merge_sort(arr, 0, num, 0)
print(" ".join(list(map(str, arr))))
print(count)
