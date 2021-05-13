s = int(input())
A = [] 
m = 0
for i in range(1,1000001):
    if i == 1:
       A.append(s)
    else:
        if A[i - 2] % 2 == 0:
            if A[i - 2] / 2 in A:
                m = i
                break
            A.append(A[i - 2] / 2)
        else:
            if 3 * A[i - 2] + 1 in A:
                m = i
                break
            A.append(3 * A[i - 2] + 1)

print(m)