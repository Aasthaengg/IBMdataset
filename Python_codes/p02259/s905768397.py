def bubbleSort(A, N):
    flag = 1
    count = 0
    while flag:
        flag = 0
        for j in reversed(xrange(1, N)):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = 1
                count+=1
    return count

# MAIN
N = input()
A = map(int, raw_input().split())
c = bubbleSort(A, N)
for i in A: print i,
print 
print c