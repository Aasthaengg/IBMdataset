n = raw_input()
A = map(int, raw_input().split())
for i in range(0, len(A)):
        if i == len(A)-1:
            print A[i]
        else:
            print A[i],
            
for i in range(1, len(A)):
    j = i - 1
    tmp = A[i]
    while A[j] > tmp and j >= 0:
        tmp2 = A[j]
        A[j] = tmp
        A[j+1] = tmp2
        j -= 1
        
    for i in range(0, len(A)):
        if i == len(A)-1:
            print A[i]
        else:
            print A[i],