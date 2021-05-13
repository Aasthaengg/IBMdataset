array = list(map(int, input().split()))
num = 3
def print_array():
    for i in range(num):
        if i != num-1:
            print(array[i], end=' ')
        else:
            print(array[i])
# insertion sort
for i in range(num):
    insert = array[i]
    j = 0
    while array[j] < insert:
        j+=1
    for k in range(i, j, -1):
        array[k] = array[k - 1]
    array[j] = insert
print_array()

