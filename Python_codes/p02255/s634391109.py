def get_input():
    length = int(raw_input())
    return map(int, raw_input().split())


def insertionSort(input_array):
    print " ".join(str(each)  for each in input_array).rstrip(" ")
    for i in range(1,len(input_array)):
        key = input_array[i]
        j = i-1
        while j >= 0 and input_array[j] > key:
            input_array[j+1] = input_array[j]
            j -= 1
            input_array[j+1] = key
        print " ".join(str(each)  for each in input_array).rstrip(" ")

insertionSort(get_input())