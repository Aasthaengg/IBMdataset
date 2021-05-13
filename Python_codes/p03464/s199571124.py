k = int(input())
A = list(map(int, input().split()))
A.reverse()

L = [-1]*(k+1)
R = [-1]*(k+1)

L[0] = 2
R[0] = 2
for i in range(1, k+1):
    if L[i-1]%A[i-1] == 0 or R[i-1]%A[i-1] == 0:
        pass
    else:
        if R[i-1] - L[i-1] >= A[i-1] or L[i-1]%A[i-1]>R[i-1]%A[i-1]:
            pass
        else:
            #print(i, A[i-1], L[i-1], R[i-1])
            print(-1)
            exit()
    if L[i-1]%A[i-1] == 0:
        L[i] = (L[i-1]//A[i-1])*A[i-1]
    else:
        L[i] = (L[i-1]//A[i-1]+1)*A[i-1]
    R[i] = (R[i-1]//A[i-1])*A[i-1]+A[i-1]-1
    #print(i, L[i], R[i])

#print(L)
#print(R)
print(L[k], R[k])