global count
count = 0


def merge(num_list, left, mid, right):
    a = mid - left
    b = right - mid
    L = []
    R = []

    for i in range(a):
        L.append(num_list[left + i])
    for i in range(b):
        R.append(num_list[mid + i])

    L.append(float("inf"))
    R.append(float("inf"))

    i = 0
    j = 0
    global count

    for k in range(left, right):
        if L[i] <= R[j]:
            num_list[k] = L[i]
            i += 1
        else:
            num_list[k] = R[j]
            j += 1
        count += 1


def mergeSort(num_list, left, right):
    if left+1 < right:
        mid = (left + right) / 2
        mergeSort(num_list, left, mid)
        mergeSort(num_list, mid, right)
        merge(num_list, left, mid, right)

    return num_list


if __name__ == "__main__":
    num = raw_input()
    line = raw_input()

    num_list = line.strip().split()
    num_list = map(int, num_list)

    merge_list = mergeSort(num_list, 0, len(num_list))
    merge_list = map(str, merge_list)
    print " ".join(merge_list)
    print count