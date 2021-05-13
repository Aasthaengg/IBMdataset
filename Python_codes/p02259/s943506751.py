def bubble_sort(A):
    flag = True
    i = 0
    global count
    while flag:
        flag = False
        for j in range(i, len(A)-1):
           if A[j+1] < A[j]:
                A[j], A[j+1] = A[j+1], A[j]
                count += 1
                flag = True
        if not flag:
            i += 1
            flag = True
        if i >= len(A)-1:
            flag = False

n = int(input())
A = list(map(int, input().split()))
count = 0
bubble_sort(A)
print(*A)
print(count)
