n = int(raw_input())
A = map(int, raw_input().split(" "))
count = 0

def merge(left, right):
    global count
    
    sorted_list = list()
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1

        else:
            sorted_list.append(right[right_index])
            right_index += 1
            
        count += 1

    if left:
        sorted_list.extend(left[left_index:])
        count += len(left[left_index:])
    if right:
        sorted_list.extend(right[right_index:])
        count += len(right[right_index:])
        

    return sorted_list


    
def mergeSort(A):
    if len(A) <= 1:
        return A

    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return list(merge(left, right))

print " ".join(map(str, mergeSort(A)))
print count