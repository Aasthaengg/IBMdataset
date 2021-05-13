def show(array):
    for i in range(len(array)):
        if i != len(array) - 1:
            print(array[i], end=' ')
        else:
            print(array[i])


def selectionSort(array):
    count = 0 
    for i in range(len(array)):
        minj = i 
        flag = False
        for j in range(i, len(array)):
            if array[j] < array[minj]:
                minj = j 
                flag = True
        if flag and i != minj:
            array[i], array[minj] = [array[minj], array[i]]
            count += 1
    
    show(array)
    print(count)
    

input()
array = [int(x) for x in input().split()]
selectionSort(array)


