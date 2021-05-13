def trace(A,input_num):
    for i in range(input_num):
        if i != input_num - 1:
            print(A[i],end = " ")
        else:
            print(A[i])

def insertionSort(A,input_num):
    for i in range(input_num):
        v = A[i]
        j = i - 1
        while(j >= 0 and A[j] > v):
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        trace(A,input_num)
        
input_num = int(input())
A = list(map(int, input().split()))

insertionSort(A,input_num)
