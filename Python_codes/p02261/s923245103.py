from copy import copy

def bubbleSort(arr):
    cp_arr = copy(arr)
    indices = list(range(len(cp_arr)))
    
    finished_flag = False
    while not finished_flag:
        finished_flag = True

        for i in range(len(cp_arr)-1):
            if cp_arr[i] > cp_arr[i+1]:
                finished_flag = False

                t = cp_arr[i]
                cp_arr[i] = cp_arr[i+1]
                cp_arr[i+1] = t

                t = indices[i]
                indices[i] = indices[i+1]
                indices[i+1] = t
    return indices

def selectionSort(arr):
    cp_arr = copy(arr)
    indices = list(range(len(cp_arr)))

    for i in range(len(cp_arr)):
        min = i
        for j in range(i+1, len(cp_arr)):
            if cp_arr[j] < cp_arr[min]:
                min = j

        t = cp_arr[i]
        cp_arr[i] = cp_arr[min]
        cp_arr[min] = t

        t = indices[i]
        indices[i] = indices[min]
        indices[min] = t

    return indices

if __name__ == "__main__":
    input()
    cards = input().split()
    values = list(map(lambda x: int(x[1]), cards))
    bubbleSorted_indices = bubbleSort(values)
    selectionSorted_indices = selectionSort(values)
    bubble_stable = True
    selection_stable = True
    for i in range(len(values)-1):
        if values[bubbleSorted_indices[i]] == values[bubbleSorted_indices[i+1]] and bubbleSorted_indices[i] > bubbleSorted_indices[i+1]:
            bubble_stable = False
        if values[selectionSorted_indices[i]] == values[selectionSorted_indices[i+1]] and selectionSorted_indices[i] > selectionSorted_indices[i+1]:
            selection_stable = False
    bubble_sorted = [cards[i] for i in bubbleSorted_indices]
    selection_sorted = [cards[i] for i in selectionSorted_indices]
    print(" ".join(bubble_sorted))
    print("Stable" if bubble_stable else "Not stable") 
    print(" ".join(selection_sorted))
    print("Stable" if selection_stable else "Not stable") 



